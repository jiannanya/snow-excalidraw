# Servers and Infrastructure Components

Pre-built component recipes for infrastructure elements. Translate coordinates to your canvas position.

All use sketch style defaults. Adjust strokeColor and roughness for blueprint/clean/dark styles.

---

## Server / Node (generic)

A rectangle representing any computing node.

```json
[
  {
    "type": "rectangle",
    "id": "comp-server",
    "x": 0, "y": 0, "width": 200, "height": 100,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-server-txt", "type": "text"}],
    "seed": 20001, "version": 1, "versionNonce": 1020001,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-server-txt",
    "x": 10, "y": 30, "width": 180, "height": 40,
    "text": "Service Name", "originalText": "Service Name",
    "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-server", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 20002, "version": 1, "versionNonce": 1020002,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Cloud Zone (deployment boundary)

A frame representing a cloud region, VPC, or Kubernetes namespace.

```json
{
  "type": "frame",
  "id": "comp-cloud-zone",
  "x": 0, "y": 0, "width": 500, "height": 300,
  "name": "AWS us-east-1",
  "strokeColor": "#1864ab", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
  "roughness": 0, "opacity": 100, "angle": 0,
  "boundElements": null, "seed": 20003, "version": 1, "versionNonce": 1020003,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "updated": 1700000000000, "link": null, "locked": false, "index": null
}
```

---

## Load Balancer

A diamond shape representing a routing/balancing decision point.

```json
[
  {
    "type": "diamond",
    "id": "comp-lb",
    "x": 0, "y": 0, "width": 160, "height": 100,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-lb-txt", "type": "text"}],
    "seed": 20004, "version": 1, "versionNonce": 1020004,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-lb-txt",
    "x": 10, "y": 35, "width": 140, "height": 30,
    "text": "Load Balancer", "originalText": "Load Balancer",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-lb", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 20005, "version": 1, "versionNonce": 1020005,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Kubernetes Pod Group

Two overlapping rectangles to suggest a pod replica set.

```json
[
  {
    "type": "rectangle",
    "id": "comp-pod-bg",
    "x": 8, "y": 8, "width": 200, "height": 90,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
    "roughness": 1, "opacity": 60, "angle": 0,
    "boundElements": null, "seed": 20006, "version": 1, "versionNonce": 1020006,
    "isDeleted": false, "groupIds": ["pod-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-pod-fg",
    "x": 0, "y": 0, "width": 200, "height": 90,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-pod-txt", "type": "text"}],
    "seed": 20007, "version": 1, "versionNonce": 1020007,
    "isDeleted": false, "groupIds": ["pod-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-pod-txt",
    "x": 10, "y": 30, "width": 180, "height": 30,
    "text": "Pod: api-server", "originalText": "Pod: api-server",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-pod-fg", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 20008, "version": 1, "versionNonce": 1020008,
    "isDeleted": false, "groupIds": ["pod-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## External System (dashed ellipse)

Represents a third-party or external service.

```json
{
  "type": "ellipse",
  "id": "comp-external",
  "x": 0, "y": 0, "width": 160, "height": 80,
  "strokeColor": "#868e96", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
  "roughness": 1, "opacity": 100, "angle": 0,
  "boundElements": [{"id": "comp-external-txt", "type": "text"}],
  "seed": 20009, "version": 1, "versionNonce": 1020009,
  "isDeleted": false, "groupIds": [], "frameId": null,
  "updated": 1700000000000, "link": null, "locked": false, "index": null
}
```
