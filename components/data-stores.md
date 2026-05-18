# Data Store Components

Pre-built component recipes for databases, caches, queues, and object storage elements.

---

## Database (cylinder simulation)

Simulated with two stacked rectangles and an ellipse cap.

```json
[
  {
    "type": "rectangle",
    "id": "comp-db-body",
    "x": 0, "y": 20, "width": 160, "height": 100,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-db-txt", "type": "text"}],
    "seed": 40001, "version": 1, "versionNonce": 1040001,
    "isDeleted": false, "groupIds": ["db-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-db-top",
    "x": 0, "y": 0, "width": 160, "height": 40,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40002, "version": 1, "versionNonce": 1040002,
    "isDeleted": false, "groupIds": ["db-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-db-txt",
    "x": 10, "y": 55, "width": 140, "height": 30,
    "text": "PostgreSQL", "originalText": "PostgreSQL",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-db-body", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40003, "version": 1, "versionNonce": 1040003,
    "isDeleted": false, "groupIds": ["db-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Cache (dashed rectangle)

```json
[
  {
    "type": "rectangle",
    "id": "comp-cache",
    "x": 0, "y": 0, "width": 160, "height": 80,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-cache-txt", "type": "text"}],
    "seed": 40010, "version": 1, "versionNonce": 1040010,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-cache-txt",
    "x": 10, "y": 28, "width": 140, "height": 24,
    "text": "Redis Cache", "originalText": "Redis Cache",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-cache", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40011, "version": 1, "versionNonce": 1040011,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Message Queue (elongated ellipse)

```json
[
  {
    "type": "ellipse",
    "id": "comp-queue",
    "x": 0, "y": 0, "width": 200, "height": 70,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-queue-txt", "type": "text"}],
    "seed": 40020, "version": 1, "versionNonce": 1040020,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-queue-txt",
    "x": 20, "y": 23, "width": 160, "height": 24,
    "text": "Kafka Topic", "originalText": "Kafka Topic",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-queue", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40021, "version": 1, "versionNonce": 1040021,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Object Store (bucket icon — two rectangles)

```json
[
  {
    "type": "rectangle",
    "id": "comp-bucket-body",
    "x": 0, "y": 16, "width": 140, "height": 100,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-bucket-txt", "type": "text"}],
    "seed": 40030, "version": 1, "versionNonce": 1040030,
    "isDeleted": false, "groupIds": ["bucket-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-bucket-lid",
    "x": -10, "y": 0, "width": 160, "height": 24,
    "strokeColor": "#1e1e1e", "backgroundColor": "#dee2e6",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40031, "version": 1, "versionNonce": 1040031,
    "isDeleted": false, "groupIds": ["bucket-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-bucket-txt",
    "x": 10, "y": 55, "width": 120, "height": 24,
    "text": "S3 Bucket", "originalText": "S3 Bucket",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-bucket-body", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 40032, "version": 1, "versionNonce": 1040032,
    "isDeleted": false, "groupIds": ["bucket-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```
