# Alexandria Dashboard

## Library Health

```dataview
TABLE length(rows) AS count FROM "10-Library/notes" GROUP BY type
```

```dataview
TABLE length(rows) AS count FROM "10-Library/notes" GROUP BY status
```

## Notes without Connections

```dataview
LIST FROM "10-Library/notes"
WHERE !contains(file.content, "## Connections")
SORT file.name ASC
```

## Seeds (needs expansion)

```dataview
LIST FROM "10-Library/notes"
WHERE status = "seed" AND type = "atomic"
SORT file.name ASC
```

## Hot Potato Active

```dataview
TABLE disciplines, status FROM "10-Library/notes"
WHERE hp = true AND status != "evergreen"
SORT title ASC
```

## Recent notes

```dataview
TABLE created FROM "10-Library/notes"
WHERE created >= date(today) - dur(7 days)
SORT created DESC
```
