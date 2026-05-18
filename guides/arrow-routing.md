# Arrow Routing Guide

Rules and recipes for connecting elements with correctly-routed arrows in Excalidraw JSON.

---

## Anatomy of an Arrow

```json
{
  "type": "arrow",
  "id": "arr-a-b",
  "x": <start_x>, "y": <start_y>,
  "width": <dx>, "height": <dy>,
  "points": [[0, 0], [<dx>, <dy>]],
  "startBinding": { "elementId": "rect-a", "gap": 5, "focus": 0 },
  "endBinding":   { "elementId": "rect-b", "gap": 5, "focus": 0 },
  "endArrowhead": "arrow",
  "startArrowhead": null,
  "strokeColor": "#1e1e1e",
  "strokeWidth": 2,
  "roughness": 1
}
```

Both bound shapes must list this arrow in their `boundElements`:

```json
{ "id": "arr-a-b", "type": "arrow" }
```

---

## Straight vs Curved vs Elbowed

| `points` count | Visual result |
|----------------|---------------|
| 2 (`[[0,0],[dx,dy]]`) | Straight diagonal |
| 3 (`[[0,0],[dx/2,0],[dx,dy]]`) | Single-elbow (horizontal then vertical) |
| 4+ | Multi-segment path |

For horizontal or vertical flows, use 2-point arrows and align coordinates exactly.

For cross-direction flows, use a 3-point elbow to route around shapes.

---

## Routing Patterns

### Pattern 1: Horizontal chain (left-to-right)

Shapes arranged in a row, arrows go straight right:

```
Shape A  ──►  Shape B  ──►  Shape C
(x=80)       (x=380)       (x=680)
```

Arrow from A → B:
```json
{
  "x": 280, "y": 160,
  "points": [[0, 0], [100, 0]],
  "startBinding": {"elementId": "rect-a", "gap": 5, "focus": 0},
  "endBinding":   {"elementId": "rect-b", "gap": 5, "focus": 0}
}
```

### Pattern 2: Vertical chain (top-to-bottom)

```
Shape A
  │
  ▼
Shape B
```

Arrow from A → B (shapes at same x):
```json
{
  "x": 180, "y": 200,
  "points": [[0, 0], [0, 80]],
  "startBinding": {"elementId": "rect-a", "gap": 5, "focus": 0},
  "endBinding":   {"elementId": "rect-b", "gap": 5, "focus": 0}
}
```

### Pattern 3: Diagonal (top-left → bottom-right)

```json
{
  "x": 280, "y": 200,
  "points": [[0, 0], [240, 160]],
  "startBinding": {"elementId": "rect-a", "gap": 5, "focus": 0},
  "endBinding":   {"elementId": "rect-b", "gap": 5, "focus": 0}
}
```

### Pattern 4: Elbow (right then down)

```
Shape A ──► turn
              │
              ▼
           Shape B
```

```json
{
  "x": 280, "y": 160,
  "points": [[0, 0], [120, 0], [120, 160]],
  "startBinding": {"elementId": "rect-a", "gap": 5, "focus": 0},
  "endBinding":   {"elementId": "rect-b", "gap": 5, "focus": 0}
}
```

### Pattern 5: Bidirectional (double-headed)

```json
{
  "endArrowhead": "arrow",
  "startArrowhead": "arrow"
}
```

### Pattern 6: Return / back edge

For back edges in a flow (cycle), route the arrow below the shapes:

```json
{
  "x": 180, "y": 240,
  "points": [[0, 0], [0, 80], [-360, 80], [-360, 0]],
  "strokeStyle": "dashed"
}
```

---

## Gap and Focus

| Field | Meaning | Recommended value |
|-------|---------|-------------------|
| `gap` | Distance from arrow tip to shape border | `5` (default) |
| `focus` | Attachment point along shape edge (-1 to 1) | `0` = center, `0.5` = quarter from center |

Use `focus: 0` for most arrows. Use non-zero focus only when multiple arrows attach to the same shape edge:

```json
"startBinding": {"elementId": "rect-a", "gap": 5, "focus": -0.3}
"startBinding": {"elementId": "rect-a", "gap": 5, "focus":  0.3}
```

---

## Arrow Label

Floating text near the midpoint of the arrow:

```json
{
  "type": "text",
  "id": "lbl-arr-a-b",
  "x": <mid_x - 40>, "y": <mid_y - 20>,
  "width": 80, "height": 16,
  "text": "HTTP 200",
  "fontSize": 13,
  "containerId": null,
  "autoResize": true
}
```

Position the label 20 px above the arrow midpoint for horizontal arrows, or 10 px to the left for vertical arrows.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `startBinding.elementId` does not exist | Check IDs, rebuild `id_map` |
| Arrow origin (`x`, `y`) does not match shape edge | Set `x`, `y` to the exit point of the source shape |
| Shapes have no `boundElements` entry for the arrow | Add `{"id": "<arrow-id>", "type": "arrow"}` |
| Arrow point count < 2 | Always use at least 2 points |
| Overlapping points (zero-length arrow) | Ensure end point ≠ start point |
