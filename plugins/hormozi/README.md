# hormozi

A Claude Code plugin with the `hormozi` skill: diagnoses a business and reviews its marketing, sales and pricing by the method of Alex Hormozi. Answers in the language of the request.

**Install** from the marketplace, in Claude Code:

```
/plugin marketplace add Londeren/claude-plugins
/plugin install hormozi@Londeren
```

If the install summary says `Run /reload-plugins to activate.`, run that command.

The other install routes (claude.ai, skills.sh, a manual copy) are described in the [marketplace README](https://github.com/Londeren/claude-plugins#installation).

**Diagnosis**: for a situation such as "not enough leads", "the ads stopped paying back" or "the business depends on me", names what is broken and what to fix first, then gives at most three steps, each with the rule of the method behind it and your numbers set against its threshold. **Review**: an offer, an ad, a sales script, a price list, a money model, a lead-nurture sequence or a retention plan; findings by severity, each with a quote from the material and the rule behind it, and a verdict on what to do first. **Rewrite**: on request, after the diagnosis, rebuilds the material by the method; your facts, numbers and prices carry over unchanged, and what the request does not give is marked for you to fill in rather than guessed. Hiring and management, org design and personal finance are out of scope.

**Built on** Alex Hormozi's books $100M Offers (2021), $100M Leads (2023) and $100M Money Models (2025); then $100M Series: Lost Chapters, the ACQ Closer Handbook, the ACQ Advertising Handbook and seven $100M Playbooks (Pricing, Price Raise, Lead Nurture, Retention, Lifetime Value, Fast Cash, GOATed Ads, all 2025); and, for enterprise value only, fragments of four video transcripts. Where they diverge, the source earlier in this list wins, and the videos never overrule the books. Full texts of the sources are not in the repository. The working build (source map, extraction catch, validation, evals) lives in the [pipeline/hormozi](https://github.com/Londeren/bookshelf-skills/tree/main/pipeline/hormozi) directory of the bookshelf-skills repository; pipeline statistics, eval results and the limits of the checks are in [PROVENANCE.md](skills/hormozi/PROVENANCE.md). License: [MIT](LICENSE).

The project is unofficial and not affiliated with Alex Hormozi or Acquisition.com; the name refers to the method.
