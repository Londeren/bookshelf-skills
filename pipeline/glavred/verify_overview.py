#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка числовых утверждений pipeline/glavred/BOOK_OVERVIEW.md с источниками в tmp/.

Запуск из корня репозитория:

    python3 pipeline/glavred/verify_overview.py        полный вывод
    python3 pipeline/glavred/verify_overview.py -q     только несовпадения и итог

Как устроено. Для каждого утверждения ОЖИДАЕМОЕ число берётся из текста самого
артефакта регулярным выражением по нужному разделу, ФАКТИЧЕСКОЕ получается
командой по источнику, дальше числа сравниваются. Поэтому проверяется не число
само по себе, а число под своей подписью: если подпись перепишут, а число нет
(или наоборот) — сверка это увидит.

Если утверждение в артефакте не найдено или найдено больше одного раза, это
несовпадение, а не пропуск: иначе переформулировка текста молча выключала бы
проверку и итог оставался бы зелёным.

Зависимости: python3 и штатные утилиты macOS (bash, grep, awk, sed, sort, wc).
Команды выполняются с LC_ALL=en_US.UTF-8: в локали C у grep -i не работает
свёртка регистра кириллицы и «например» находится 75 раз вместо 217.

Коды возврата: 0 — всё совпало, 1 — есть несовпадения, 2 — нет источников
или артефакта (tmp/ в .gitignore, у постороннего человека источников не будет).
"""

import os
import re
import shlex
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACT = os.path.join(ROOT, "pipeline", "glavred", "BOOK_OVERVIEW.md")

SRC = {
    "S1": "tmp/Пиши, сокращай 2025_ Как создавать сильный текст mineru.md",
    "S2": "tmp/Ясно, понятно_ Как доносить мысли и убеждать людей mineru.md",
    "S3": "tmp/Большая книга о соцсетях для предпринимателей, экспертов mineru.md",
    "S4": "tmp/сильный текст.md",
}

# Разделы артефакта, внутри которых ищутся утверждения. Ограничение по разделу
# нужно, чтобы одинаковые формулировки в паспортах разных источников не путались.
REGION_BOUNDS = {
    "р3": "## 3. Свойства mineru-конвертации",
    "S1": "## 4. Источник 1",
    "S2": "## 5. Источник 2",
    "S3": "## 6. Источник 3",
    "S4": "## 7. Источник 4",
    "р9": "## 9. Механическая сверка карты",
}


# --------------------------------------------------------------------------
# инфраструктура
# --------------------------------------------------------------------------

def die(msg, code=2):
    print(msg, file=sys.stderr)
    sys.exit(code)


def preflight():
    if not os.path.exists(ARTIFACT):
        die("Не найден артефакт %s — сверять нечего." % ARTIFACT)
    missing = [p for p in SRC.values() if not os.path.exists(os.path.join(ROOT, p))]
    if missing:
        print("Источники не найдены, сверка не выполнялась.", file=sys.stderr)
        print("Ожидались файлы (относительно %s):" % ROOT, file=sys.stderr)
        for p in missing:
            print("  нет: %s" % p, file=sys.stderr)
        print(
            "\nКаталог tmp/ в .gitignore и в репозиторий не попадает — это нормально.\n"
            "Положите исходные .md в tmp/ под этими именами и запустите снова:\n"
            "  python3 pipeline/glavred/verify_overview.py",
            file=sys.stderr,
        )
        sys.exit(2)


def sh(cmd):
    """Выполнить команду через bash. Ненулевой код возврата не считается
    ошибкой: grep -c при нуле совпадений печатает 0 и выходит с кодом 1."""
    env = dict(os.environ, LC_ALL="en_US.UTF-8")
    r = subprocess.run(["/bin/bash", "-c", cmd], cwd=ROOT, env=env,
                       capture_output=True, text=True)
    out = r.stdout.strip()
    if not out and r.returncode not in (0, 1):
        return "<ошибка команды: %s>" % (r.stderr.strip().splitlines() or ["?"])[0]
    return out


def q(path_or_text):
    return shlex.quote(path_or_text)


ART_TEXT = None
REGIONS = {}


def load_artifact():
    global ART_TEXT
    ART_TEXT = open(ARTIFACT, encoding="utf-8").read()
    marks = sorted(
        ((ART_TEXT.index(h), name, h) for name, h in REGION_BOUNDS.items()
         if h in ART_TEXT),
        key=lambda t: t[0],
    )
    heads = [m.start() for m in re.finditer(r"(?m)^## ", ART_TEXT)]
    for pos, name, _ in marks:
        nxt = [h for h in heads if h > pos]
        REGIONS[name] = ART_TEXT[pos:nxt[0] if nxt else len(ART_TEXT)]
    for name in REGION_BOUNDS:
        if name not in REGIONS:
            die("В артефакте нет раздела %r (искали строку %r)."
                % (name, REGION_BOUNDS[name]))


class NotFound(Exception):
    pass


def claim(region, pattern, group=1):
    """Достать ожидаемое число из артефакта. Ровно одно совпадение — иначе ошибка."""
    hits = re.findall(pattern, REGIONS[region])
    if len(hits) != 1:
        raise NotFound("утверждение %s в разделе %s: совпадений %d, нужно ровно 1"
                       % (pattern, region, len(hits)))
    hit = hits[0]
    return hit[group - 1] if isinstance(hit, tuple) else hit


def num(s):
    """Нормализация числа: убрать разделители разрядов, запятую привести к точке."""
    s = str(s).strip()
    for ch in (" ", " ", " ", " "):
        s = s.replace(ch, "")
    return s.replace(",", ".")


# --------------------------------------------------------------------------
# разбор карт нарезки (нужен двум сводным проверкам)
# --------------------------------------------------------------------------

_MAP_CACHE = None


def map_rows():
    """Строки карт нарезки: id, источник, диапазон строк, заявленный размер,
    все заголовки в обратных кавычках (адрес секции и точки дробления).

    Берутся только таблицы под «### Карта нарезки»: одноимённую разметку
    `| N.M |` имеет ещё и таблица сверки в разделе 9, её брать нельзя."""
    global _MAP_CACHE
    if _MAP_CACHE is not None:
        return _MAP_CACHE
    rows, inmap = [], False
    for line in ART_TEXT.split("\n"):
        if line.startswith("### Карта нарезки"):
            inmap = True
            continue
        if inmap and (line.startswith("## ") or line.startswith("---")):
            inmap = False
        if not inmap or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.match(r"^([1-4])\.(\d+)$", cells[0])
        if not m or len(cells) != 6:
            continue
        rng = re.match(r"^(\d+)[–-](\d+)$", cells[2])
        if not rng:
            continue
        rows.append({
            "id": cells[0],
            "src": "S" + m.group(1),
            "a": int(rng.group(1)),
            "b": int(rng.group(2)),
            "size": cells[3],
            "label": cells[4].replace("*", "").strip(),
            "headers": [h for h in re.findall(r"`([^`]+)`", line) if h.startswith("#")],
        })
    _MAP_CACHE = rows
    return rows


def label_count(src, label):
    """Строк карты источника с точно этой меткой (выделение ** снимается)."""
    return sum(1 for r in map_rows()
               if r["src"] == src and r["label"] == label)


_SIZE_CACHE = None


def map_sizes():
    """Сверка колонки ~байт с фактическим объёмом диапазона строк."""
    global _SIZE_CACHE
    if _SIZE_CACHE is not None:
        return _SIZE_CACHE
    sized, off = 0, []
    for r in map_rows():
        m = re.match(r"^([\d,]+)k$", r["size"])
        if not m:
            continue
        sized += 1
        claimed = float(m.group(1).replace(",", ".")) * 1000
        actual = int(sh("sed -n '%d,%dp' %s | wc -c" % (r["a"], r["b"], q(SRC[r["src"]]))))
        if actual and abs(actual - claimed) / actual > 0.05:
            off.append((r["id"], r["size"], actual))
    _SIZE_CACHE = (sized, off)
    return _SIZE_CACHE


def sizes_detail():
    return ["строка карты %s: в колонке %s, фактически %d байт (строки %s)"
            % (i, s, a, next("%d–%d" % (r["a"], r["b"])
                             for r in map_rows() if r["id"] == i))
            for i, s, a in map_sizes()[1]]


def addresses_detail():
    return ["строка карты %s: заголовок %r не найден дословно в диапазоне "
            "(встречается в строках %s)" % (i, h, hits or "нигде")
            for i, h, hits in map_addresses()[1]]


_ADDR_CACHE = None


def map_addresses():
    """Каждый заголовок из карт ищется как точное совпадение целой строки
    в своём источнике; найденный номер строки должен лежать в диапазоне строки карты."""
    global _ADDR_CACHE
    if _ADDR_CACHE is not None:
        return _ADDR_CACHE
    total, bad = 0, []
    for r in map_rows():
        for h in r["headers"]:
            total += 1
            out = sh("grep -nxF -- %s %s" % (q(h), q(SRC[r["src"]])))
            hits = [int(x.split(":", 1)[0]) for x in out.splitlines()
                    if x.split(":", 1)[0].isdigit()]
            if not any(r["a"] <= x <= r["b"] for x in hits):
                bad.append((r["id"], h, hits[:5]))
    _ADDR_CACHE = (total, bad)
    return _ADDR_CACHE


# --------------------------------------------------------------------------
# список проверок
# --------------------------------------------------------------------------

CHECKS = []


def add(name, region, pattern, cmd=None, group=1, fn=None, cmd_text=None,
        detail=None):
    CHECKS.append(dict(name=name, region=region, pattern=pattern, group=group,
                       cmd=cmd, fn=fn, cmd_text=cmd_text or cmd, detail=detail))


def build_checks():
    f = {k: q(v) for k, v in SRC.items()}

    # --- класс 1: паспорта и таблица раздела 9 -----------------------------
    tbl = {
        "S1": r"\| Пиши, сокращай 2025 \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|",
        "S2": r"\| Ясно, понятно \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|",
        "S3": r"\| Большая книга о соцсетях \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|",
        "S4": r"\| Сильный текст \(рассылка\) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|",
    }
    cols = [
        (1, "заголовков всего", "grep -c '^#' %s"),
        (2, "заголовков `#`", "grep -c '^# ' %s"),
        (3, "заголовков `##`", "grep -c '^## ' %s"),
        (4, "заголовков `###`", "grep -c '^### ' %s"),
        (5, "строк в файле", "wc -l < %s"),
    ]
    for s in ("S1", "S2", "S3", "S4"):
        for g, what, cmd in cols:
            add("%s: %s (раздел 9, таблица)" % (s, what), "р9", tbl[s],
                cmd % f[s], group=g)
        add("%s: размер файла в байтах (паспорт)" % s, s,
            r"`tmp/[^`]+`, ([\d\u00a0 ]+) байт", "wc -c < %s" % f[s])

    # --- класс 2: размеры выпусков и секций --------------------------------
    issue_sizes = ("awk '/^# File name:/{if(NR>1)print s; s=0} {s+=length($0)+1} "
                   "END{print s}' %s" % f["S4"])
    add("S4: минимальный размер выпуска, байт", "S4",
        r"от ([\d\u00a0 ]+) до [\d\u00a0 ]+ байт",
        issue_sizes + " | sort -n | head -1")
    add("S4: максимальный размер выпуска, байт", "S4",
        r"от [\d\u00a0 ]+ до ([\d\u00a0 ]+) байт",
        issue_sizes + " | sort -n | tail -1")
    add("S4: выпусков короче 2000 байт", "S4",
        r"короче 2000 байт — (\d+)",
        issue_sizes + " | awk '$1<2000' | wc -l")
    add("S4: выпусков длиннее 25 000 байт", "S4",
        r"длиннее 25[  ]000 байт — (\d+)",
        issue_sizes + " | awk '$1>25000' | wc -l")
    add("S4: выпусков крупнее порога дробления 40 000 байт", "S4",
        r"крупнее 40[  ]000 байт — (\d+)",
        issue_sizes + " | awk '$1>40000' | wc -l")
    add("S3: размер секции 3.20 (строки 3200–3215), awk", "р9",
        r"`awk` — (\d+), `wc -c` — \d+, `wc -m` — \d+",
        "sed -n '3200,3215p' %s | awk '{c+=length($0)+1} END{print c}'" % f["S3"])
    add("S3: размер секции 3.20, wc -c", "р9",
        r"`awk` — \d+, `wc -c` — (\d+), `wc -m` — \d+",
        "sed -n '3200,3215p' %s | wc -c" % f["S3"])
    add("S3: размер секции 3.20 в символах, wc -m", "р9",
        r"`awk` — \d+, `wc -c` — \d+, `wc -m` — (\d+)",
        "sed -n '3200,3215p' %s | wc -m" % f["S3"])
    add("всего строк-кандидатов в четырёх картах нарезки", "р9",
        r"В картах (\d+) строк-кандидатов",
        fn=lambda: len(map_rows()),
        cmd_text="разбор таблиц «### Карта нарезки» в артефакте")
    add("строк карт с числовым размером в колонке ~байт", "р9",
        r"у (\d+) указан числовой размер",
        fn=lambda: map_sizes()[0],
        cmd_text="для каждой строки карты: sed -n 'A,Bp' <источник> | wc -c",
        detail=sizes_detail)
    add("строк карт, где размер расходится с фактическим больше чем на 5 %", "р9",
        r"расходится с фактическим больше чем на 5 % — (\d+)",
        fn=lambda: len(map_sizes()[1]),
        cmd_text="для каждой строки карты: sed -n 'A,Bp' <источник> | wc -c",
        detail=sizes_detail)
    # не только сколько расхождений, но и какие именно: иначе починка одной
    # строки и поломка другой оставят счёт прежним и сверка пройдёт
    add("какие строки карт расходятся по размеру", "р9",
        r"больше чем на 5 % — \d+: это ([\d.]+) `",
        fn=lambda: ", ".join(i for i, _, _ in map_sizes()[1]) or "нет",
        cmd_text="список расходящихся строк карт против названного в тексте",
        detail=sizes_detail)
    add("S1: размер строк 38–56 (диапазон строки карты 1.1)", "р9",
        r"строки 38–56 занимают (\d+) байт",
        "sed -n '38,56p' %s | wc -c" % f["S1"])
    add("S1: размер строк 38–87 (оглавление целиком)", "р9",
        r"38–87 = (\d+) байт",
        "sed -n '38,87p' %s | wc -c" % f["S1"])

    # --- класс 3: частоты маркеров -----------------------------------------
    for s in ("S1", "S2"):
        add("%s: вхождений «например»" % s, s, r"«например» — (\d+) вхождени",
            "grep -oi 'например' %s | wc -l" % f[s])
        add("%s: вхождений «сравните»" % s, s, r"«сравните» — (\d+)",
            "grep -oi 'сравните' %s | wc -l" % f[s])
        add("%s: строк, начинающихся с маркера разбора" % s, s,
            r"`\^\(было\|стало\|плохо\|хорошо\)` — (\d+)",
            "grep -ciE '^(было|стало|плохо|хорошо)' %s" % f[s])
        add("%s: вхождений `ошибк[аи]`" % s, s, r"`ошибк\[аи\]` — (\d+) вхождени",
            "grep -oiE 'ошибк[аи]' %s | wc -l" % f[s])
    add("S1: вхождений запретительных оборотов", "S1",
        r"не используйте` — (\d+)",
        "grep -oiE 'не надо|нельзя|не стоит|не пишите|не используйте' %s | wc -l" % f["S1"])
    add("S2: вхождений запретительных оборотов", "S2",
        r"запретительные обороты той же командой — (\d+)",
        "grep -oiE 'не надо|нельзя|не стоит|не пишите|не используйте' %s | wc -l" % f["S2"])

    # --- класс 4: адреса карт ----------------------------------------------
    addr_cmd = ("для каждого адреса: grep -nxF -- '<заголовок>' <источник>, "
                "номер строки сверяется с диапазоном строки карты")
    add("адресов-заголовков в картах, проверено", "р9",
        r"адресов-заголовков в картах: (\d+) / проблемных: \d+",
        fn=lambda: map_addresses()[0], cmd_text=addr_cmd,
        detail=addresses_detail)
    add("адресов, не найденных дословно в своём диапазоне", "р9",
        r"адресов-заголовков в картах: \d+ / проблемных: (\d+)",
        fn=lambda: len(map_addresses()[1]), cmd_text=addr_cmd,
        detail=addresses_detail)

    # --- класс 4а: раскладка меток карт ------------------------------------
    # сами метки — суждение и скриптом не проверяются; проверяются выведенные
    # из них счёты, которыми проза «Где ядро» описывает карту
    lbl = "подсчёт колонки «Метка» в таблицах «### Карта нарезки»"
    add("S1: строк в карте нарезки", "S1",
        r"Ядро — \d+ строк карты из (\d+)",
        fn=lambda: sum(1 for r in map_rows() if r["src"] == "S1"), cmd_text=lbl)
    add("S1: строк с меткой «ядро» (без частичного)", "S1",
        r"Ядро — (\d+) строк карты из \d+",
        fn=lambda: label_count("S1", "ядро"), cmd_text=lbl)
    add("S2: строк в карте нарезки", "S2",
        r"подавляющая часть книги: \d+ строки карты из (\d+)",
        fn=lambda: sum(1 for r in map_rows() if r["src"] == "S2"), cmd_text=lbl)
    add("S2: строк с меткой «ядро» (без частичного)", "S2",
        r"подавляющая часть книги: (\d+) строки карты из \d+",
        fn=lambda: label_count("S2", "ядро"), cmd_text=lbl)
    add("S4: строк в карте нарезки", "S4",
        r"в карте (\d+) строк, из них",
        fn=lambda: sum(1 for r in map_rows() if r["src"] == "S4"), cmd_text=lbl)
    add("S4: строк с меткой «ядро»", "S4",
        r"Ядро — (\d+) писем из 113",
        fn=lambda: label_count("S4", "ядро"), cmd_text=lbl)

    # --- класс 5: счёт писем рассылки --------------------------------------
    add("S4: служебных строк `# File name:` (писем)", "р9",
        r"`grep -c '\^# File name:'` → (\d+) писем",
        "grep -c '^# File name:' %s" % f["S4"])
    add("S4: заголовков уровня `#` всего", "р9",
        r"`grep -c '\^# '` → (\d+) заголовков",
        "grep -c '^# ' %s" % f["S4"])
    add("S4: номерных заголовков выпусков", "р9",
        r"`grep -c '\^# \[0-9\]'` → (\d+) номерных",
        "grep -c '^# [0-9]' %s" % f["S4"])
    add("S4: служебных писем без номера", "р9",
        r"`grep -c '\^# \[\^0-9F\]'` → (\d+) служебных",
        "grep -c '^# [^0-9F]' %s" % f["S4"])

    # --- класс 6: артефакты конвертации ------------------------------------
    hyph = "grep -oE '[а-яёА-ЯЁ]- [а-яё]' %s | wc -l"
    for i, s in enumerate(("S1", "S2", "S3", "S4"), start=1):
        add("%s: разрывов мягкого переноса" % s, "р3",
            r"S1 — (\d+) случаев, S2 — (\d+), S3 — (\d+), S4 — (\d+)",
            hyph % f[s], group=i)
        add("%s: строк с неразрывным пробелом U+00A0" % s, "р9",
            r"S1 — (\d+) строк, S2 — (\d+), S3 — (\d+), S4 — (\d+)",
            "grep -c $'\\xc2\\xa0' %s" % f[s], group=i)
        add("%s: картинок-плейсхолдеров" % s, "р3",
            r"S1 — (\d+) картинок, S2 — (\d+), S3 — (\d+), S4 — (\d+)",
            "grep -c '!\\[' %s" % f[s], group=i)
        add("%s: строк с комбинирующим U+0306 (NFD)" % s, "р9",
            r"даёт (\d+) / (\d+) / (\d+) / (\d+) строк", "grep -c $'\\xcc\\x86' %s" % f[s],
            group=i)
    add("S4: гиперссылок в рассылке", "S4", r"(\d+) рабочих гиперссылок",
        "grep -o '](http' %s | wc -l" % f["S4"])
    # число, которым раздел 9 показывает ловушку локали: та же команда в C
    add("S1: вхождений «например» в локали C (ловушка)", "р9",
        r"находит (\d+) вхождений вместо 217",
        "LC_ALL=C grep -oi 'например' %s | wc -l" % f["S1"])

    # --- класс 7: пересчёт байт в символы ----------------------------------
    ratio = ("awk -v b=\"$(wc -c < %s)\" -v m=\"$(wc -m < %s)\" "
             "'BEGIN{printf \"%%.3f\\n\", b/m}'")
    for i, s in enumerate(("S1", "S2", "S3", "S4"), start=1):
        add("%s: отношение байт к символам" % s, "S1",
            r"S1 — (\d,\d+), S2 — (\d,\d+), S3 — (\d,\d+), S4 — (\d,\d+)",
            ratio % (f[s], f[s]), group=i)
    add("коэффициент пересчёта назван одинаково в разделах 4 и 9", "S1",
        r"символы ≈ байты ÷ (\d,\d+)",
        fn=lambda: claim("р9", r"делением на (\d,\d+)"),
        cmd_text="сверка двух мест самого артефакта, где назван коэффициент")

    # --- класс 8: сверка самого заявления ----------------------------------
    add("число сверок, заявленное в разделе 9", "р9", r"`совпало (\d+) из \d+`",
        fn=lambda: len(CHECKS),
        cmd_text="итоговая строка этого скрипта")


# --------------------------------------------------------------------------
# прогон
# --------------------------------------------------------------------------

def main():
    quiet = "-q" in sys.argv or "--quiet" in sys.argv
    preflight()
    load_artifact()
    build_checks()

    print("Сверка чисел: pipeline/glavred/BOOK_OVERVIEW.md против источников в tmp/")
    print("Ожидаемое берётся из текста артефакта, фактическое — из источника.")
    print("")

    ok_count = 0
    for i, c in enumerate(CHECKS, start=1):
        try:
            expected = claim(c["region"], c["pattern"], c["group"])
        except NotFound as e:
            expected = "<НЕ НАЙДЕНО: %s>" % e
        actual = str(c["fn"]()) if c["fn"] else sh(c["cmd"])
        good = not expected.startswith("<") and num(expected) == num(actual)
        ok_count += good
        if quiet and good:
            continue
        print("%02d  утверждение: %s" % (i, c["name"]))
        print("    команда:     %s" % c["cmd_text"])
        print("    в артефакте: %s | фактически: %s | %s"
              % (expected, actual, "совпало" if good else "НЕ СОВПАЛО"))
        if not good and c["detail"]:
            rows = c["detail"]()
            for row in rows[:10]:
                print("      · %s" % row)
            if len(rows) > 10:
                print("      · …и ещё %d" % (len(rows) - 10))
            if not rows:
                print("      · расхождений не найдено")

    print("")
    print("итог: совпало %d из %d" % (ok_count, len(CHECKS)))
    if ok_count != len(CHECKS):
        print("есть несовпадения: исправьте артефакт или проверку")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
