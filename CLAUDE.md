# CLAUDE.md

Guidance for Claude Code working on this repository.

## What this is

A shelf of domain skills for Claude. Each plugin carries one author's method, distilled from a book or several; today that is `glavred-skill` (Maxim Ilyahov, editing social media posts). Every method is a plugin of its own, so a user installs only the ones they need. A plugin may hold more than one skill of its method, such as the `-apply` and `-diagnose` pair that book-to-skill allows for a rich source; skills of different methods never share a plugin.

Skills are built with the book-to-skill pipeline from [Londeren/claude-plugins](https://github.com/Londeren/claude-plugins). Meta-skills, the ones that build or improve other prompts and skills, live there and never here.

This repository has no marketplace manifest. The catalog is `.claude-plugin/marketplace.json` in Londeren/claude-plugins, where every plugin from here is an entry with a `git-subdir` source. A plugin id is the plugin name followed by `@Londeren` whichever repository hosts the plugin, which is how `glavred-skill` kept its id when it moved here.

## Layout

```
plugins/<method>/                 ships to users
  .claude-plugin/plugin.json
  skills/<skill>/SKILL.md         references/ and PROVENANCE.md sit next to it
  README.md
  LICENSE
pipeline/<method>/                the build: overview, catch, validation, evals; published, not shipped
docs/superpowers/                 plans and decisions
tmp/<method>/                     sources and private eval material, in .gitignore, never committed
.superpowers/                     scratch of agent workflows, in .gitignore
```

Only `plugins/<method>/` ships. Nothing from `pipeline/`, `docs/` or `tmp/` goes inside it, and no CLAUDE.md either: the skills.sh route installs a skill folder into the user's own project, where a stray CLAUDE.md would load as their nested project instructions.

A skill lives in `plugins/<method>/skills/<skill>/SKILL.md`, never at the plugin root. The claude.ai loader takes the skill name from the folder under `skills/`; a plugin without that folder installs and exposes zero skills, and `claude plugin validate` does not catch it.

glavred predates the per-method folders under `tmp/`: its books sit at the top of `tmp/`, where `pipeline/glavred/verify_overview.py` expects them.

## Naming

`<method>` is the name of the method: latin, lowercase, hyphens, after the method or the book rather than the action, as book-to-skill's naming rule has it. One name serves the plugin, `pipeline/<method>/`, `tmp/<method>/`, and the skill too when the plugin holds a single one; a pair of skills takes suffixes, `<method>-apply` and `<method>-diagnose`. Choose the name before anything else, since every folder carries it.

glavred is the exception: its plugin is `glavred-skill`, a suffix kept only because that id was published under the old repository name, while its skill and build folders are `glavred`. New plugins take no suffix.

## Adding a skill

1. Choose the name, then work on a branch, `skill/<method>`. `main` is what both install routes read, the skills.sh CLI lists every `SKILL.md` it finds there, and book-to-skill writes the skill folder in phase 3, before the evals of phase 4. So the branch reaches `main` only after the build's self-check and evals pass, or after the user explicitly waives a gate, with the waiver recorded in PROVENANCE.md.
2. Copy the sources into `tmp/<method>/` under short plain names made from their titles: latin, lowercase, hyphens, such as `100m-offers.md`. The build records and PROVENANCE.md name the files the skill was built from, and both are public, so a download-site tag, a hash or a local path in a file name would be published with it. Plain names also keep `$`, brackets and curly quotes out of shell commands over the sources.
3. Build with book-to-skill. Its working files go to `pipeline/<method>/`; the generated skill goes to `plugins/<method>/skills/<skill>/`, with PROVENANCE.md next to its SKILL.md.
4. Add `.claude-plugin/plugin.json`, `README.md` and `LICENSE` to `plugins/<method>/`. plugin.json follows glavred's, with `homepage` pointing at the plugin folder. The plugin README is written in the language of the skill: what the skill does, what it is built from, the two Claude Code install commands, and a link to [the install routes](https://github.com/Londeren/claude-plugins#installation) for everything else.
5. Add a row to the table of this README, merge the branch into `main` and push `main`. This push comes before anything in Londeren/claude-plugins: the marketplace entry points at `main` on GitHub, and an entry pushed first would point at a path that does not exist yet.
6. In Londeren/claude-plugins: a marketplace entry with a `git-subdir` source pointing at `plugins/<method>` and an English description, plus the places in its root README that its CLAUDE.md lists. Push, then run the install check under "Checking changes".

## Publication

Plugins and their build directories are public. `pipeline/` and the anchors in a skill's reference sheets carry verbatim quotes from the books; publishing them is a deliberate decision of 2026-09-15 and overrides book-to-skill's advice to trim quotes down to addresses before a skill leaves the team. Full source texts never get committed.

Eval cases taken from the user's own practice, such as their posts or their business situations and figures, stay whole in `tmp/<method>/evals/`: the request, its assertions and the outputs produced on it. The public eval set in `pipeline/<method>/evals/` carries the synthetic cases, and the published results report practice cases by id and score only. glavred's eval set predates the rule and quotes the user's own posts, which was accepted when its pipeline was published.

A new plugin starts at version `0.1.0`. Bump `version` in a plugin.json whenever shipped files change: installed copies update by version.

## docs/

Documents under `docs/superpowers/` name the method they belong to in the filename. Historic documents keep the paths and the repository name that were true when they were written; do not retrofit them. The same holds for the records of a finished build under `pipeline/<method>/`: `pipeline/glavred/BOOK_OVERVIEW.md` still names its verification script by the path it had before the move.

`docs/superpowers/plans/2026-08-13-glavred-skill.md` is such a record, not a template. It was written for the old single-plugin layout and an older book-to-skill: take the procedure from this file and from book-to-skill itself, never paths or rules from that plan. Nor is glavred a precedent for its rejection rate: it shipped below book-to-skill's threshold on an explicit waiver recorded in its PROVENANCE.md.

## History

`main` is the public line. glavred was developed on a separate history and published as a squashed release; that development history is not on GitHub and survives only in the `dev-history` branch of the original local checkout.

## Checking changes

From the root of this repository:

```bash
claude plugin validate ./plugins/<method> --strict
git ls-files plugins | sort
python3 pipeline/glavred/verify_overview.py -q
```

The second command guards the packaging boundary on staged or committed files, which are what ships: nothing from `pipeline/`, `docs/` or `tmp/` may appear in that listing, and no CLAUDE.md. It uses `git ls-files` rather than `find`, which also lists ignored `.DS_Store` files that never ship. The third checks the figures in glavred's source overview against the books and needs them in `tmp/`.

After both repositories are pushed, install the plugin from the marketplace into a throwaway config and compare what arrived with what is committed. Run the block as one command, with the plugin name as the last argument: the variable has to reach every line, and a line run without it installs into your real `~/.claude`.

```bash
CLAUDE_CONFIG_DIR="$(mktemp -d)" bash -c '
  set -e
  claude plugin marketplace add Londeren/claude-plugins
  claude plugin install "$1@Londeren"
  diff <(cd "$CLAUDE_CONFIG_DIR"/plugins/cache/Londeren/"$1"/*/ && find . -type f -not -name .in_use | sed "s|^\./||" | sort) \
       <(git ls-files "plugins/$1" | sed "s|^plugins/$1/||" | sort)
  echo "installed files match the repository"
' _ <plugin>
```
