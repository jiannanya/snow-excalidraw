# Element Recipes

Ready-to-use JSON templates for every element type. Copy and customize.

All recipes use **sketch style** defaults. For blueprint/clean/dark styles, adjust strokeColor, backgroundColor, roughness, and fontFamily per the style guides in `../styles/`.

---

## Free-Floating Text (Title / Heading)

```json
{
  "type": "text",
  "id": "txt-title",
  "x": 80, "y": 40,
  "width": 400, "height": 30,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "text": "Diagram Title",
  "originalText": "Diagram Title",
  "fontSize": 24,
  "fontFamily": 5,
  "textAlign": "left",
  "verticalAlign": "top",
  "containerId": null,
  "autoResize": true,
  "lineHeight": 1.25,
  "seed": 10001,
  "version": 1,
  "versionNonce": 1010001,
  "isDeleted": false,
  "groupIds": [],
  "frameId": null,
  "boundElements": null,
  "updated": 1700000000000,
  "link": null,
  "locked": false,
  "index": null
}
```

---

## Rectangle (Process / Service / Step)

```json
{
  "type": "rectangle",
  "id": "rect-step-1",
  "x": 80, "y": 120,
  "width": 200, "height": 80,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "seed": 10002,
  "version": 1,
  "versionNonce": 1010002,
  "isDeleted": false,
  "groupIds": [],
  "frameId": null,
  "boundElements": [{"id": "txt-step-1", "type": "text"}],
  "updated": 1700000000000,
  "link": null,
  "locked": false,
  "index": null
}
```

---

## Bound Text (inside a shape)

```json
{
  "type": "text",
  "id": "txt-step-1",
  "x": 90, "y": 150,
  "width": 180, "height": 25,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "text": "Step Name",
  "originalText": "Step Name",
  "fontSize": 16,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "rect-step-1",
  "autoResize": true,
  "lineHeight": 1.25,
  "seed": 10003,
  "version": 1,
  "versionNonce": 1010003,
  "isDeleted": false,
  "groupIds": [],
  "frameId": null,
  "boundElements": null,
  "updated": 1700000000000,
  "link": null,
  "locked": false,
  "index": null
}
```

---

## Ellipse (Actor / Entry / Concept)

```json
{
  "type": "ellipse",
  "id": "ellipse-actor",
  "x": 80, "y": 120,
  "width": 160, "height": 80,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "seed": 10004, "version": 1, "versionNonce": 1010004,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": [{"id": "txt-actor", "type": "text"}],
  "updated": 1700000000000, "link": null, "locked": false, "index": null
}
```

---

## Diamond (Decision Node)

```json
{
  "type": "diamond",
  "id": "diamond-gate",
  "x": 360, "y": 120,
  "width": 160, "height": 100,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "seed": 10005, "version": 1, "versionNonce": 1010005,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": [{"id": "txt-gate", "type": "text"}],
  "updated": 1700000000000, "link": null, "locked": false, "index": null
}
```

---

## Arrow (Directed Connection)

```json
{
  "type": "arrow",
  "id": "arrow-a-to-b",
  "x": 282, "y": 160,
  "width": 80, "height": 0,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "points": [[0, 0], [80, 0]],
  "startBinding": { "elementId": "rect-step-1", "gap": 5, "focus": 0 },
  "endBinding": { "elementId": "diamond-gate", "gap": 5, "focus": 0 },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "seed": 10006, "version": 1, "versionNonce": 1010006,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null, "updated": 1700000000000,
  "link": null, "locked": false, "index": null
}
```

**Bent arrow (3+ points):**
```json
{
  "points": [[0, 0], [40, 0], [40, 80], [120, 80]]
}
```

---

## Line (Structural, Non-Directional)

```json
{
  "type": "line",
  "id": "line-spine",
  "x": 80, "y": 200,
  "width": 800, "height": 0,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "points": [[0, 0], [800, 0]],
  "startArrowhead": null,
  "endArrowhead": null,
  "seed": 10007, "version": 1, "versionNonce": 1010007,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null, "updated": 1700000000000,
  "link": null, "locked": false, "index": null
}
```

---

## Frame (Grouping Container)

```json
{
  "type": "frame",
  "id": "frame-zone-a",
  "x": 60, "y": 80,
  "width": 400, "height": 300,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "name": "Zone A",
  "seed": 10008, "version": 1, "versionNonce": 1010008,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null, "updated": 1700000000000,
  "link": null, "locked": false, "index": null
}
```

---

## Milestone Dot (for timelines)

```json
{
  "type": "ellipse",
  "id": "dot-milestone-1",
  "x": 188, "y": 194,
  "width": 16, "height": 16,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#1e1e1e",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "seed": 10009, "version": 1, "versionNonce": 1010009,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null, "updated": 1700000000000,
  "link": null, "locked": false, "index": null
}
```

---

## Layout Grid Reference

Use this grid for positioning. Canvas: 1400 × 900px.

```
       col1    col2    col3    col4    col5    col6
row1   80,80   300,80  520,80  740,80  960,80  1180,80
row2   80,200  300,200 520,200 740,200 960,200 1180,200
row3   80,320  300,320 520,320 740,320 960,320 1180,320
row4   80,440  300,440 520,440 740,440 960,440 1180,440
row5   80,560  300,560 520,560 740,560 960,560 1180,560
row6   80,680  300,680 520,680 740,680 960,680 1180,680
row7   80,800  300,800 520,800 740,800 960,800 1180,800
```

Standard element sizes:
- Rectangle: `width: 200, height: 80`
- Ellipse: `width: 160, height: 80`
- Diamond: `width: 160, height: 100`
- Arrow: starts at `source.x + source.width + 5`, ends at `target.x - 5`
