# ER Diagram (Entity-Relationship)

Guide for drawing database schema / entity-relationship diagrams in Excalidraw JSON.

---

## When to Use

Use an ER diagram when the request mentions:

- Database tables, columns, primary keys, foreign keys
- Schema design, data model, relational model
- "What does the DB look like?", "Show entities and relations"
- ORM models (Django, SQLAlchemy, Prisma, TypeORM)

---

## Layout Rules

| Strategy | When to apply |
|----------|---------------|
| **Grid** | 3–6 tables, balanced relationships |
| **Hub-and-spoke** | One central table (e.g., `orders`) with many dependents |
| **Left-to-right** | Linear lookup chains |

Canvas: **1800 × 1000 px**. Table width: **220 px**. Column height: **30 px** per row. Gap between tables: **180 px**.

---

## Entity Table Element

Each entity is a group of stacked rectangles:

### Table header (entity name)

```json
{
  "type": "rectangle",
  "id": "tbl-users-header",
  "x": 80, "y": 120,
  "width": 220, "height": 40,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#1971c2",
  "fillStyle": "solid",
  "roughness": 1,
  "boundElements": [{"id": "lbl-users-header", "type": "text"}]
}
```

Header label (white text on blue):

```json
{
  "type": "text",
  "id": "lbl-users-header",
  "x": 90, "y": 130,
  "width": 200, "height": 20,
  "text": "users",
  "fontSize": 16,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "tbl-users-header",
  "autoResize": true,
  "strokeColor": "#ffffff"
}
```

### Column row (PK / FK highlighted)

```json
{
  "type": "rectangle",
  "id": "col-users-id",
  "x": 80, "y": 160,
  "width": 220, "height": 30,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#fff9db",
  "fillStyle": "solid",
  "roughness": 0,
  "boundElements": [{"id": "lbl-users-id", "type": "text"}]
}
```

Column label `PK  id  INT`:

```json
{
  "type": "text",
  "id": "lbl-users-id",
  "x": 88, "y": 168,
  "width": 204, "height": 14,
  "text": "PK  id  INT",
  "fontSize": 13,
  "fontFamily": 3,
  "textAlign": "left",
  "verticalAlign": "middle",
  "containerId": "col-users-id",
  "autoResize": true
}
```

Regular column row (no fill):

```json
{
  "type": "rectangle",
  "id": "col-users-email",
  "x": 80, "y": 190,
  "width": 220, "height": 30,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "roughness": 0,
  "boundElements": [{"id": "lbl-users-email", "type": "text"}]
}
```

---

## Relationship Arrow

| Relationship type | Arrow style |
|-------------------|-------------|
| One-to-many (1:N) | `endArrowhead: "arrow"`, `startArrowhead: null` |
| Many-to-many (M:N) | `endArrowhead: "arrow"`, `startArrowhead: "arrow"` |
| One-to-one (1:1) | `endArrowhead: "bar"`, `startArrowhead: "bar"` |
| Optional (0..) | Use `strokeStyle: "dashed"` |

```json
{
  "type": "arrow",
  "id": "rel-users-orders",
  "x": 300, "y": 175,
  "points": [[0, 0], [180, 0]],
  "strokeColor": "#1e1e1e",
  "strokeWidth": 2,
  "endArrowhead": "arrow",
  "startArrowhead": null,
  "roughness": 1,
  "startBinding": {"elementId": "tbl-users-header", "gap": 5, "focus": 0},
  "endBinding":   {"elementId": "tbl-orders-header", "gap": 5, "focus": 0}
}
```

Add a cardinality label near each arrow end:

```json
{
  "type": "text",
  "id": "card-1",
  "x": 306, "y": 160,
  "width": 20, "height": 14,
  "text": "1",
  "fontSize": 13,
  "containerId": null,
  "autoResize": true
}
```

---

## Color Conventions

| Purpose | Background |
|---------|-----------|
| Entity header | `#1971c2` (blue) with white text |
| Primary key row | `#fff9db` (yellow) |
| Foreign key row | `#e7f5ff` (light blue) |
| Regular column | `transparent` |

---

## Example: 3-Table Schema

Tables: `users` → `orders` → `order_items`

Position `users` at x=80, `orders` at x=400, `order_items` at x=720.
Each table is ~4–6 rows tall → height 40 + (rows × 30) px.

---

## Animation Sequence (`animseq.json`)

Reveal tables entity by entity:

```json
{
  "startMs": 400,
  "defaultDuration": 400,
  "elements": [
    {"id": "tbl-users-header",  "order": 1, "duration": 300},
    {"id": "col-users-id",      "order": 1, "duration": 200},
    {"id": "col-users-email",   "order": 1, "duration": 200},
    {"id": "tbl-orders-header", "order": 2, "duration": 300},
    {"id": "col-orders-id",     "order": 2, "duration": 200},
    {"id": "rel-users-orders",  "order": 3, "duration": 500}
  ]
}
```
