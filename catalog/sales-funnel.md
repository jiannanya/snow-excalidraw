# Sales Funnel

Guide for drawing sales funnel and conversion pipeline diagrams in Excalidraw JSON.

---

## When to Use

Use a sales funnel when the request mentions:

- Conversion rate, drop-off, funnel stages
- Lead pipeline, MQL → SQL → Opportunity → Closed
- Marketing funnel: Awareness → Interest → Desire → Action
- Customer journey with quantified counts at each stage
- Product activation funnel (sign-up → trial → paid)

---

## Layout: Stacked Trapezoids (top-down)

Each stage is a **trapezoid** drawn as a polygon using `freedraw` or constructed from a rectangle with a frame. Because Excalidraw lacks a native trapezoid, use **stacked rectangles with decreasing widths** to approximate a funnel shape.

Canvas: **1800 × 1000 px**

| Stage | Y start | Width | X offset (to center) |
|-------|---------|-------|-----------------------|
| 1 (top) | 80 | 800 | 500 |
| 2 | 220 | 640 | 580 |
| 3 | 360 | 480 | 660 |
| 4 | 500 | 320 | 740 |
| 5 (bottom) | 640 | 160 | 820 |

Stage height: **120 px**. Subtract 20 px from each side per stage.

---

## Stage Rectangle

```json
{
  "type": "rectangle",
  "id": "stage-1",
  "x": 500, "y": 80,
  "width": 800, "height": 120,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#1971c2",
  "fillStyle": "solid",
  "roughness": 1,
  "boundElements": [{"id": "lbl-stage-1", "type": "text"}]
}
```

Stage label:

```json
{
  "type": "text",
  "id": "lbl-stage-1",
  "x": 510, "y": 118,
  "width": 780, "height": 44,
  "text": "Awareness  —  10 000 visitors",
  "fontSize": 20,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "stage-1",
  "autoResize": true,
  "strokeColor": "#ffffff"
}
```

---

## Color Progression (top → bottom)

| Stage | `backgroundColor` |
|-------|------------------|
| 1 (widest) | `#1971c2` (blue) |
| 2 | `#1c7ed6` |
| 3 | `#339af0` |
| 4 | `#74c0fc` |
| 5 (narrowest) | `#a5d8ff` |

Darken for "dark" style; keep pastel for "clean" style.

---

## Conversion Rate Annotation

Place a text element to the right of the gap between stages:

```json
{
  "type": "text",
  "id": "rate-1-2",
  "x": 1320, "y": 180,
  "width": 160, "height": 30,
  "text": "↓ 38% conversion",
  "fontSize": 14,
  "fontFamily": 1,
  "strokeColor": "#495057",
  "containerId": null,
  "autoResize": true
}
```

Arrow pointing left from the annotation to the funnel edge:

```json
{
  "type": "arrow",
  "id": "arr-rate-1-2",
  "x": 1318, "y": 195,
  "points": [[0, 0], [-18, 0]],
  "strokeColor": "#adb5bd",
  "endArrowhead": "arrow",
  "roughness": 0
}
```

---

## Horizontal Funnel Variant

For a left-to-right pipeline (common for B2B sales):
- Rotate the stage structure 90°
- Stage widths become heights: top stage is tallest, bottom is shortest
- Add pipeline arrows between stages

Column positions: x = 60, 340, 620, 900, 1180 (each column 240 px wide).

---

## Animation Sequence (`animseq.json`)

Reveal from top (wide) to bottom (narrow):

```json
{
  "startMs": 500,
  "defaultDuration": 500,
  "elements": [
    {"id": "stage-1", "order": 1, "duration": 400},
    {"id": "lbl-stage-1", "order": 1, "duration": 300},
    {"id": "stage-2", "order": 2, "duration": 400},
    {"id": "rate-1-2", "order": 2, "duration": 300},
    {"id": "stage-3", "order": 3, "duration": 400},
    {"id": "stage-4", "order": 4, "duration": 400},
    {"id": "stage-5", "order": 5, "duration": 400}
  ]
}
```
