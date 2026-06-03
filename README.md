# GameDevWiki

A compounding, LLM-assisted **game design research wiki** — atomic notes distilled from 17 canonical game design books, cross-source syntheses, reference sheets, and game analyses.

Built and maintained in [Obsidian](https://obsidian.md), published here so it can be read and navigated directly on GitHub. Every link below is clickable.

---

## Start here

- **By discipline** — the maps of content in [`00-Atlas/disciplines`](00-Atlas/disciplines): [Mechanics](00-Atlas/disciplines/Mechanics.md) · [Feel & Controls](00-Atlas/disciplines/Feel%20%26%20Controls.md) · [Player](00-Atlas/disciplines/Player.md) · [Level Design](00-Atlas/disciplines/Level%20Design.md) · [Narrative](00-Atlas/disciplines/Narrative.md) · [Theory](00-Atlas/disciplines/Theory.md) · [Production](00-Atlas/disciplines/Production.md) · [Interface](00-Atlas/disciplines/Interface.md) · [Business](00-Atlas/disciplines/Business.md)
- **By cross-cutting theme** — the bridges in [`00-Atlas/bridges`](00-Atlas/bridges) (e.g. [Flow & Mental Models](00-Atlas/bridges/Flow%20%26%20Mental%20Models.md), [Mechanics across the canon](00-Atlas/bridges/Mechanics%20across%20the%20canon.md)).
- **Topic syntheses** — [`05-Syntheses`](05-Syntheses): one page per topic, weaving together what every source says.
- **Reference sheets** — [`20-Reference`](20-Reference): [Schell's Lenses by Chapter](20-Reference/Schell%20Lenses%20by%20Chapter.md), [Mechanics Reference](20-Reference/Mechanics%20Reference.md), and more.

## How it's organized

| Folder | What's inside |
|---|---|
| [`00-Atlas`](00-Atlas) | Maps of content — entry points by discipline and by theme |
| [`05-Syntheses`](05-Syntheses) | Cross-source topic syntheses |
| [`10-Library`](10-Library) | 178 atomic notes (`notes/`) + one page per source book (`sources/`) |
| [`20-Reference`](20-Reference) | Scannable reference sheets (lenses, taxonomies) |
| [`30-Analyses`](30-Analyses) | Game and genre analyses |

## About the sources

The 17 source books are summarised into original notes — **the books themselves are not included** (the `raw/` PDFs are git-ignored for copyright). Each note cites its source so you can find the original. See [`10-Library/sources`](10-Library/sources) for the bibliography.

---

## Notes for editors

This vault is written in Obsidian using `[[wikilinks]]`, which GitHub does not render as clickable links. The script [`_tools/github_export.py`](_tools/github_export.py) converts them in place to relative Markdown links (`[text](path.md)`) that work in **both** Obsidian and GitHub. It is idempotent — re-run it after adding content:

```bash
python _tools/github_export.py
```

Links it cannot resolve (e.g. notes that don't exist yet) are left as `[[...]]` and reported, so broken references stay visible.
