---
type: moc
discipline: <discipline-slug>
tags: [moc]
---

# <Emoji> <Discipline> — Map of Content

**Start here:** [[note-1]] → [[note-2]] → [[note-3]] → [[note-4]]

## All <discipline> notes

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "<discipline-slug>") SORT title ASC
```

## Bridges

- [[../bridges/<BridgeName>]]
