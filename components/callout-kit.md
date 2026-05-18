# Callout Kit Components

Pre-built component recipes for annotations, badges, callouts, and information markers.

---

## Warning Badge

A small diamond or triangle-ish shape with a "!" marker.

```json
[
  {
    "type": "diamond",
    "id": "comp-warning-shape",
    "x": 0, "y": 0, "width": 40, "height": 40,
    "strokeColor": "#e67700", "backgroundColor": "#fff9db",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-warning-txt", "type": "text"}],
    "seed": 60001, "version": 1, "versionNonce": 1060001,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-warning-txt",
    "x": 12, "y": 10, "width": 16, "height": 20,
    "text": "!", "originalText": "!",
    "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-warning-shape", "autoResize": false, "lineHeight": 1.25,
    "strokeColor": "#e67700", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 60002, "version": 1, "versionNonce": 1060002,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Success Tick Callout

A small ellipse with a checkmark.

```json
[
  {
    "type": "ellipse",
    "id": "comp-success-shape",
    "x": 0, "y": 0, "width": 36, "height": 36,
    "strokeColor": "#2f9e44", "backgroundColor": "#ebfbee",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-success-txt", "type": "text"}],
    "seed": 60010, "version": 1, "versionNonce": 1060010,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-success-txt",
    "x": 6, "y": 8, "width": 24, "height": 20,
    "text": "✓", "originalText": "✓",
    "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-success-shape", "autoResize": false, "lineHeight": 1.25,
    "strokeColor": "#2f9e44", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 60011, "version": 1, "versionNonce": 1060011,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Annotation Bubble (speech bubble style)

A rectangle with a pointed bottom-left edge annotation.

```json
[
  {
    "type": "rectangle",
    "id": "comp-bubble",
    "x": 10, "y": 0, "width": 220, "height": 60,
    "strokeColor": "#1e1e1e", "backgroundColor": "#fff9db",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-bubble-txt", "type": "text"}],
    "seed": 60020, "version": 1, "versionNonce": 1060020,
    "isDeleted": false, "groupIds": ["bubble-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-bubble-txt",
    "x": 18, "y": 10, "width": 204, "height": 40,
    "text": "Annotation text here", "originalText": "Annotation text here",
    "fontSize": 13, "fontFamily": 1,
    "textAlign": "left", "verticalAlign": "middle",
    "containerId": "comp-bubble", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 60021, "version": 1, "versionNonce": 1060021,
    "isDeleted": false, "groupIds": ["bubble-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Error / Dead End Marker

A rectangle with red stroke and "×" label.

```json
[
  {
    "type": "ellipse",
    "id": "comp-error-shape",
    "x": 0, "y": 0, "width": 36, "height": 36,
    "strokeColor": "#c92a2a", "backgroundColor": "#fff5f5",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-error-txt", "type": "text"}],
    "seed": 60030, "version": 1, "versionNonce": 1060030,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-error-txt",
    "x": 5, "y": 8, "width": 26, "height": 20,
    "text": "×", "originalText": "×",
    "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-error-shape", "autoResize": false, "lineHeight": 1.25,
    "strokeColor": "#c92a2a", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 60031, "version": 1, "versionNonce": 1060031,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```
