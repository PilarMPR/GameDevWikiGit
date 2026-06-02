# Alexandria — Content Catalog

Auto-generated via Dataview. Last manual update: 2026-06-02. For navigation, use [[../00-Atlas/🏛 Alexandria]].

---

## Sources (17)

```dataview
TABLE id, title, author, year, status, hp_relevance FROM "10-Library/sources"
WHERE type != "moc"
SORT id ASC
```

---

## Atomic Notes by Discipline

### Mechanics

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "mechanics") AND type = "atomic"
SORT title ASC
```

### Player

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "player") AND type = "atomic"
SORT title ASC
```

### Theory

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "theory") AND type = "atomic"
SORT title ASC
```

### Feel & Controls

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "feel-and-controls") AND type = "atomic"
SORT title ASC
```

### Level Design

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "level-design") AND type = "atomic"
SORT title ASC
```

### Production

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "production") AND type = "atomic"
SORT title ASC
```

### Narrative

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "narrative") AND type = "atomic"
SORT title ASC
```

### Interface

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "interface") AND type = "atomic"
SORT title ASC
```

### Business

```dataview
TABLE sources, status FROM "10-Library/notes"
WHERE contains(disciplines, "business") AND type = "atomic"
SORT title ASC
```

---

## Schell Lenses

```dataview
TABLE lens, title FROM "10-Library/notes"
WHERE lens >= 1 AND lens <= 100
SORT lens ASC
```

---

## Entities

```dataview
TABLE title, role FROM "10-Library/notes"
WHERE type = "entity"
SORT title ASC
```

---

## Hot Potato Library

```dataview
TABLE disciplines, sources FROM "10-Library/notes"
WHERE hp = true AND type = "atomic"
SORT title ASC
```
