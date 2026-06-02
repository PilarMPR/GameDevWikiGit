# Dashboard

> Última actualización: generado por Claude Code · usa Dataview

---

## Hot Potato — Workspace activo

### Sprint activo — tareas pendientes

```dataview
TASK
FROM "HotPotato/production"
WHERE !completed
GROUP BY section
```

### GDD

```dataview
TABLE file.mtime as "Modificado"
FROM "HotPotato"
WHERE startswith(file.name, "gdd-")
SORT file.name ASC
```

### Producción y finanzas

```dataview
LIST
FROM "HotPotato"
WHERE contains(list("production", "finance"), file.name)
SORT file.name ASC
```

### Decisiones y preguntas abiertas

```dataview
LIST
FROM "HotPotato"
WHERE contains(list("decisions", "open-questions", "research", "Brainstorming"), file.name)
SORT file.name ASC
```

---

## News Feed — Últimas entradas

```dataview
TABLE date as "Fecha", source as "Fuente", hp_relevance as "Hot Potato"
FROM "wiki/feed"
WHERE file.name != "_template"
SORT date DESC
LIMIT 10
```

---

## Wiki — Páginas modificadas recientemente

```dataview
TABLE file.folder as "Sección", dateformat(file.mtime, "yyyy-MM-dd") as "Modificado"
FROM "wiki"
SORT file.mtime DESC
LIMIT 12
```

---

## Fuentes ingresadas (17)

```dataview
TABLE dateformat(file.mtime, "yyyy-MM-dd") as "Ingresado"
FROM "wiki/sources"
SORT file.name ASC
```

---

## Concept Compendium

### Mechanics & Systems

```dataview
LIST
FROM "wiki/concepts/mechanics"
SORT file.name ASC
```

### Feel & Controls

```dataview
LIST
FROM "wiki/concepts/feel-and-controls"
SORT file.name ASC
```

### Player & Psychology

```dataview
LIST
FROM "wiki/concepts/player"
SORT file.name ASC
```

### Narrative

```dataview
LIST
FROM "wiki/concepts/narrative"
SORT file.name ASC
```

### Level Design

```dataview
LIST
FROM "wiki/concepts/level-design"
SORT file.name ASC
```

### Production

```dataview
LIST
FROM "wiki/concepts/production"
SORT file.name ASC
```

### Programming

```dataview
LIST
FROM "wiki/concepts/programming"
SORT file.name ASC
```

### Art & Technical Art

```dataview
LIST
FROM "wiki/concepts/art-tech"
SORT file.name ASC
```

### Theory

```dataview
LIST
FROM "wiki/concepts/theory"
SORT file.name ASC
```

### Interface

```dataview
LIST
FROM "wiki/concepts/interface"
SORT file.name ASC
```

### Business

```dataview
LIST
FROM "wiki/concepts/business"
SORT file.name ASC
```

### Legacy stubs (raíz de concepts/)

```dataview
LIST
FROM "wiki/concepts"
WHERE file.folder = "wiki/concepts"
SORT file.name ASC
```

---

## Entidades

```dataview
LIST
FROM "wiki/entities"
SORT file.name ASC
```

---

## Síntesis

```dataview
LIST
FROM "wiki/syntheses"
SORT file.name ASC
```
