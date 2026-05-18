# Interface Components

Pre-built component recipes for UI surface representations — browser chrome, mobile frames, desktop windows.

---

## Browser Chrome Frame

A rectangle with a small header bar to suggest a browser window.

```json
[
  {
    "type": "rectangle",
    "id": "comp-browser-outer",
    "x": 0, "y": 0, "width": 320, "height": 240,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30001, "version": 1, "versionNonce": 1030001,
    "isDeleted": false, "groupIds": ["browser-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-browser-bar",
    "x": 0, "y": 0, "width": 320, "height": 32,
    "strokeColor": "#1e1e1e", "backgroundColor": "#f1f3f5",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30002, "version": 1, "versionNonce": 1030002,
    "isDeleted": false, "groupIds": ["browser-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-browser-url",
    "x": 40, "y": 8, "width": 240, "height": 18,
    "text": "https://example.com", "originalText": "https://example.com",
    "fontSize": 12, "fontFamily": 1,
    "textAlign": "left", "verticalAlign": "top",
    "containerId": null, "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#495057", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30003, "version": 1, "versionNonce": 1030003,
    "isDeleted": false, "groupIds": ["browser-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-browser-dot1",
    "x": 10, "y": 10, "width": 10, "height": 10,
    "strokeColor": "#1e1e1e", "backgroundColor": "#1e1e1e",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30004, "version": 1, "versionNonce": 1030004,
    "isDeleted": false, "groupIds": ["browser-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Mobile Screen Frame

A tall rounded rectangle to suggest a smartphone screen.

```json
[
  {
    "type": "rectangle",
    "id": "comp-mobile-outer",
    "x": 0, "y": 0, "width": 200, "height": 360,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30010, "version": 1, "versionNonce": 1030010,
    "isDeleted": false, "groupIds": ["mobile-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-mobile-status",
    "x": 0, "y": 0, "width": 200, "height": 24,
    "strokeColor": "#1e1e1e", "backgroundColor": "#f1f3f5",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30011, "version": 1, "versionNonce": 1030011,
    "isDeleted": false, "groupIds": ["mobile-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-mobile-notch",
    "x": 80, "y": 6, "width": 40, "height": 14,
    "strokeColor": "#1e1e1e", "backgroundColor": "#1e1e1e",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30012, "version": 1, "versionNonce": 1030012,
    "isDeleted": false, "groupIds": ["mobile-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Desktop Window Frame

A rectangle with a title bar strip.

```json
[
  {
    "type": "rectangle",
    "id": "comp-desktop-outer",
    "x": 0, "y": 0, "width": 480, "height": 320,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30020, "version": 1, "versionNonce": 1030020,
    "isDeleted": false, "groupIds": ["desktop-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-desktop-titlebar",
    "x": 0, "y": 0, "width": 480, "height": 36,
    "strokeColor": "#1e1e1e", "backgroundColor": "#dee2e6",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-desktop-title", "type": "text"}],
    "seed": 30021, "version": 1, "versionNonce": 1030021,
    "isDeleted": false, "groupIds": ["desktop-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-desktop-title",
    "x": 140, "y": 8, "width": 200, "height": 20,
    "text": "Application Name", "originalText": "Application Name",
    "fontSize": 13, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-desktop-titlebar", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 30022, "version": 1, "versionNonce": 1030022,
    "isDeleted": false, "groupIds": ["desktop-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```
