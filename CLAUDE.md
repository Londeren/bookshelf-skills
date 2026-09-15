# CLAUDE.md

Guidance for Claude Code working on this repository.

## What this is

A shelf of domain skills for Claude. Each skill carries one author's method, distilled from a book or several; today that is `glavred-skill` (Maxim Ilyahov, editing social media posts). Every skill is a plugin of its own, so a user installs only the ones they need.

Skills are built with the book-to-skill pipeline from [Londeren/claude-plugins](https://github.com/Londeren/claude-plugins). Meta-skills, the ones that build or improve other prompts and skills, live there and never here.

This repository has no marketplace manifest. The catalog is `.claude-plugin/marketplace.json` in Londeren/claude-plugins, where every plugin from here is an entry with a `git-subdir` source. A plugin id is `<name>@Londeren` whichever repository hosts the plugin, which is how `glavred-skill` kept its id when it moved here.

## Layout

```
plugins/<name>/                 ships to users
  .claude-plugin/plugin.json
  skills/<skill>/SKILL.md       references/ and PROVENANCE.md sit next to it
  README.md
  LICENSE
pipeline/<skill>/               the build: overview, catch, validation, evals; published, not shipped
docs/superpowers/               plans and decisions
tmp/                            source exports, in .gitignore, never committed
```

Only `plugins/<name>/` ships. Nothing from `pipeline/`, `docs/` or `tmp/` goes inside it, and no CLAUDE.md either: the skills.sh route installs a skill folder into the user's own project, where a stray CLAUDE.md would load as their nested project instructions.

A skill lives in `plugins/<plugin>/skills/<skill>/SKILL.md`, never at the plugin root. The claude.ai loader takes the skill name from the folder under `skills/`; a plugin without that folder installs and exposes zero skills, and `claude plugin validate` does not catch it.

Each skill keeps its sources in `tmp/<skill>/`. glavred predates that rule: its books sit at the top of `tmp/`, where `pipeline/glavred/verify_overview.py` expects them.

## Adding a skill

1. Build it with book-to-skill. The working files of the build go to `pipeline/<skill>/`, PROVENANCE.md next to the generated SKILL.md.
2. Create `plugins/<name>/` with `.claude-plugin/plugin.json`, `skills/<skill>/`, `README.md` and `LICENSE` only once the skill has real content. The skills.sh CLI discovers skills by walking the repository for `SKILL.md` files, so a placeholder shows up in the public listing the moment it is pushed.
3. In Londeren/claude-plugins: a marketplace entry with a `git-subdir` source pointing at `plugins/<name>`, a row in the plugin table of its root README, and the install routes there.
4. A row in the table of this README.

## Publication

Plugins and their build directories are public. `pipeline/` carries verbatim quotes from the books as anchors; publishing them is a deliberate decision of 2026-09-15 and overrides book-to-skill's advice to trim quotes down to addresses before a skill leaves the team. Full source texts never get committed.

Bump `version` in a plugin.json whenever shipped files change: installed copies update by version.

## docs/

Documents under `docs/superpowers/` name the skill they belong to in the filename. Historic documents keep the paths and the repository name that were true when they were written; do not retrofit them. The same holds for the records of a finished build under `pipeline/<skill>/`: `pipeline/glavred/BOOK_OVERVIEW.md` still names its verification script by the path it had before the move.

## History

`main` is the public line. glavred was developed on a separate history and published as a squashed release; that development history is not on GitHub and survives only in the `dev-history` branch of the original local checkout.

## Checking changes

```bash
claude plugin validate ./plugins/<name> --strict
find plugins -type f | sort
python3 pipeline/glavred/verify_overview.py -q
```

The second command guards the packaging boundary: nothing from `pipeline/`, `docs/` or `tmp/` may appear in that listing, and no CLAUDE.md. The third checks the figures in glavred's source overview against the books and needs them in `tmp/`.
