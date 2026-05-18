# Sequence Diagram

Guide for drawing UML-style sequence diagrams in Excalidraw JSON.

---

## When to Use

Use a sequence diagram when the request mentions:

- Message passing between services, actors, or components
- API call chains, HTTP request / response flows
- Protocol handshakes, auth flows (OAuth, SSO)
- WebSocket or event-driven interactions
- "Show me how A calls B calls C"

---

## Layout Rules

| Axis | Role |
|------|------|
| **Horizontal (X)** | Each actor / lifeline column |
| **Vertical (Y)** | Time — increases downward |

Canvas: **1800 × 1000 px**. Lifeline columns spaced **240 px** apart starting at x = 120.

### Column positions for up to 6 actors

| Lifeline | X center |
|----------|----------|
| 1st | 120 |
| 2nd | 360 |
| 3rd | 600 |
| 4th | 840 |
| 5th | 1080 |
| 6th | 1320 |

---

## Element Breakdown

### Actor box (rectangle)

```json
{
  "type": "rectangle",
  "id": "actor-client",
  "x": 20, "y": 60,
  "width": 200, "height": 50,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#e7f5ff",
  "fillStyle": "solid",
  "roughness": 1,
  "boundElements": [{"id": "lbl-client", "type": "text"}]
}
```

### Lifeline (dashed vertical line)

```json
{
  "type": "line",
  "id": "life-client",
  "x": 120, "y": 110,
  "points": [[0, 0], [0, 700]],
  "strokeColor": "#adb5bd",
  "strokeStyle": "dashed",
  "roughness": 0
}
```

### Synchronous message (solid arrow, left to right)

```json
{
  "type": "arrow",
  "id": "msg-1",
  "x": 120, "y": 180,
  "points": [[0, 0], [240, 0]],
  "strokeColor": "#1e1e1e",
  "strokeWidth": 2,
  "endArrowhead": "arrow",
  "startArrowhead": null,
  "roughness": 1,
  "startBinding": {"elementId": "life-client", "gap": 0, "focus": 0},
  "endBinding":   {"elementId": "life-server", "gap": 0, "focus": 0}
}
```

### Return message (dashed arrow, right to left)

```json
{
  "type": "arrow",
  "id": "msg-2-ret",
  "x": 360, "y": 280,
  "points": [[0, 0], [-240, 0]],
  "strokeColor": "#495057",
  "strokeStyle": "dashed",
  "endArrowhead": "arrow",
  "startArrowhead": null,
  "roughness": 0
}
```

### Activation box (narrow rectangle on lifeline)

```json
{
  "type": "rectangle",
  "id": "act-server-1",
  "x": 352, "y": 175,
  "width": 16, "height": 110,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#fff9db",
  "fillStyle": "solid",
  "roughness": 0
}
```

### Message label (free-floating text above arrow)

```json
{
  "type": "text",
  "id": "lbl-msg-1",
  "x": 140, "y": 160,
  "width": 200, "height": 18,
  "text": "GET /api/data",
  "fontSize": 14,
  "fontFamily": 1,
  "containerId": null,
  "autoResize": true
}
```

---

## Row Spacing Guidelines

| Step type | Vertical gap from previous row |
|-----------|-------------------------------|
| First message | 180 px from actor boxes |
| Synchronous call + return pair | 100 px per pair |
| Self-message loop | 80 px |
| Alt / loop frame header | add 30 px above |

---

## Alt / Loop Frame

Draw a rectangle enclosing the conditional rows:

```json
{
  "type": "rectangle",
  "id": "frame-alt",
  "x": 60, "y": 320,
  "width": 560, "height": 180,
  "strokeColor": "#339af0",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeStyle": "dashed",
  "roughness": 0
}
```

Place a small label `[alt]` or `[loop 3x]` at the top-left corner of the frame.

---

## Animation Sequence (`animseq.json`)

For sequence diagrams, animate one message at a time:

```json
{
  "startMs": 400,
  "defaultDuration": 400,
  "elements": [
    {"id": "actor-client", "order": 1, "duration": 300},
    {"id": "actor-server", "order": 1, "duration": 300},
    {"id": "life-client",  "order": 2, "duration": 200},
    {"id": "life-server",  "order": 2, "duration": 200},
    {"id": "msg-1",        "order": 3, "duration": 500},
    {"id": "lbl-msg-1",    "order": 3, "duration": 300},
    {"id": "act-server-1", "order": 4, "duration": 200},
    {"id": "msg-2-ret",    "order": 5, "duration": 500}
  ]
}
```

**Rule:** actor boxes first → lifelines together → each message in send order.
