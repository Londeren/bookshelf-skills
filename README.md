# Bookshelf Skills

Skills for Claude built from books. Each one carries a single author's method, distilled with the [book-to-skill](https://github.com/Londeren/claude-plugins/tree/main/plugins/book-to-skill) pipeline: every rule is anchored in a verbatim quote from the source and checked against it.

## Skills

| Plugin | What it does | Docs |
|---|---|---|
| **glavred-skill** | Reviews and edits social media posts by the method of Maxim Ilyahov. Reports findings level by level (meaning, delivery, wording, format) with a quote from the post and the rule behind each one, or rewrites the post keeping the author's facts and voice. Works in Russian | [plugins/glavred-skill](plugins/glavred-skill/README.md) |

Every method is a plugin of its own, so you install only the ones you need.

## Installation

The plugins are listed in the [Londeren marketplace](https://github.com/Londeren/claude-plugins#installation), which describes every install route: Claude Code, claude.ai, the skills.sh CLI and a manual copy. In Claude Code, with a plugin name from the table above:

```
/plugin marketplace add Londeren/claude-plugins
/plugin install <plugin>@Londeren
```

## Repository layout

```
plugins/<method>/               - a plugin, ships to users
  .claude-plugin/plugin.json    - plugin manifest
  skills/<skill>/               - the skill itself; the folder name is the skill name
    SKILL.md                    - entry point, the only file loaded on activation
    references/                 - reference sheets, read on demand
    PROVENANCE.md               - how the skill was built, never loaded
  README.md                     - the plugin's own documentation
pipeline/<method>/              - the build: source overview, extraction catch,
                                  validation with rejection reasons, evals; not shipped
docs/                           - plans and decisions, not shipped
CLAUDE.md                       - instructions for Claude Code working on this repository
```

Full texts of the books are not in the repository. The build directories quote them verbatim, since every extracted rule carries its anchor.

The skills are unofficial and not affiliated with the authors of the books.

## License

[MIT](LICENSE)
