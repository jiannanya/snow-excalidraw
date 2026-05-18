# Kanban Board

Guide for drawing Kanban-style workflow boards in Excalidraw JSON.

---

## When to Use

Use a Kanban board when the request mentions:

- Task boards, sprint boards, Jira-like boards
- Work-in-progress limits, WIP columns
- "Show tasks moving through stages"
- Swim lanes, status columns (To Do / In Progress / Done)
- Team workflow visualisation

---

## Layout Rules

Canvas: **1800 × 1000 px**

| Element | Sizing |
|---------|--------|
| Column width | **280 px** |
| Column gap | **30 px** → columns start at x = 60, 370, 680, 990, 1300 |
| Column header height | **50 px** |
| Card height | **80 px** |
| Card gap (vertical) | **12 px** |
| First card Y | column header bottom + 16 px |

---

## Column Elements

### Column background lane

```json
{
  "type": "rectangle",
  "id": "lane-todo",
  "x": 60, "y": 60,
  "width": 280, "height": 860,
  "strokeColor": "#dee2e6",
  "backgroundColor": "#f8f9fa",
  "fillStyle": "solid",
  "roughness": 0,
  "strokeStyle": "solid"
}
```

### Column header

```json
{
  "type": "rectangle",
  "id": "hdr-todo",
  "x": 60, "y": 60,
  "width": 280, "height": 50,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#1971c2",
  "fillStyle": "solid",
  "roughness": 1,
  "boundElements": [{"id": "lbl-hdr-todo", "type": "text"}]
}
```

Header label:

```json
{
  "type": "text",
  "id": "lbl-hdr-todo",
  "x": 70, "y": 70,
  "width": 260, "height": 30,
  "text": "📋 To Do",
  "fontSize": 16,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "hdr-todo",
  "autoResize": true,
  "strokeColor": "#ffffff"
}
```

---

## Card Elements

### Task card

```json
{
  "type": "rectangle",
  "id": "card-1",
  "x": 72, "y": 126,
  "width": 256, "height": 80,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#ffffff",
  "fillStyle": "solid",
  "roughness": 1,
  "boundElements": [{"id": "lbl-card-1", "type": "text"}]
}
```

Card label (multi-line OK):

```json
{
  "type": "text",
  "id": "lbl-card-1",
  "x": 80, "y": 134,
  "width": 240, "height": 40,
  "text": "Design login screen\n#UX",
  "fontSize": 14,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "middle",
  "containerId": "card-1",
  "autoResize": true
}
```

---

## Priority Color Coding

| Priority | Card `backgroundColor` |
|----------|----------------------|
| High / Blocker | `#fff5f5` (red tint) |
| Medium | `#fff9db` (yellow tint) |
| Low | `#f8f9fa` (neutral) |
| Done / Completed | `#ebfbee` (green tint) |

---

## WIP Limit Badge

Place a small ellipse on the column header to show WIP limit:

```json
{
  "type": "ellipse",
  "id": "wip-todo",
  "x": 316, "y": 66,
  "width": 28, "height": 28,
  "strokeColor": "#e03131",
  "backgroundColor": "#fff5f5",
  "fillStyle": "solid",
  "roughness": 0,
  "boundElements": [{"id": "lbl-wip-todo", "type": "text"}]
}
```

```json
{
  "type": "text",
  "id": "lbl-wip-todo",
  "x": 316, "y": 72,
  "width": 28, "height": 16,
  "text": "3",
  "fontSize": 12,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "wip-todo",
  "autoResize": true
}
```

---

## Typical Column Set

| Column | Header color |
|--------|-------------|
| Backlog | `#868e96` (grey) |
| To Do | `#1971c2` (blue) |
| In Progress | `#e67700` (orange) |
| Review / QA | `#7048e8` (purple) |
| Done | `#2f9e44` (green) |

---

## Animation Sequence (`animseq.json`)

Reveal column by column, then cards within each:

```json
{
  "startMs": 400,
  "defaultDuration": 350,
  "elements": [
    {"id": "lane-todo",  "order": 1, "duration": 200},
    {"id": "hdr-todo",   "order": 1, "duration": 300},
    {"id": "lane-inprog","order": 2, "duration": 200},
    {"id": "hdr-inprog", "order": 2, "duration": 300},
    {"id": "card-1",     "order": 3, "duration": 300},
    {"id": "card-2",     "order": 4, "duration": 300}
  ]
}
```
