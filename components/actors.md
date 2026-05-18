# Actor Components

Pre-built component recipes for representing people, teams, and organizations.

---

## Person (stick figure style)

A simple ellipse head + labeled rectangle body.

```json
[
  {
    "type": "ellipse",
    "id": "comp-person-head",
    "x": 55, "y": 0, "width": 30, "height": 30,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50001, "version": 1, "versionNonce": 1050001,
    "isDeleted": false, "groupIds": ["person-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "rectangle",
    "id": "comp-person-body",
    "x": 40, "y": 34, "width": 60, "height": 50,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50002, "version": 1, "versionNonce": 1050002,
    "isDeleted": false, "groupIds": ["person-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-person-label",
    "x": 0, "y": 90, "width": 140, "height": 20,
    "text": "User", "originalText": "User",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "top",
    "containerId": null, "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50003, "version": 1, "versionNonce": 1050003,
    "isDeleted": false, "groupIds": ["person-group"], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## Team Group (multiple dots inside a frame)

```json
[
  {
    "type": "frame",
    "id": "comp-team-frame",
    "x": 0, "y": 0, "width": 200, "height": 100,
    "name": "Engineering Team",
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
    "roughness": 0, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50010, "version": 1, "versionNonce": 1050010,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-team-dot1",
    "x": 20, "y": 30, "width": 30, "height": 30,
    "strokeColor": "#1e1e1e", "backgroundColor": "#dee2e6",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50011, "version": 1, "versionNonce": 1050011,
    "isDeleted": false, "groupIds": [], "frameId": "comp-team-frame",
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-team-dot2",
    "x": 65, "y": 30, "width": 30, "height": 30,
    "strokeColor": "#1e1e1e", "backgroundColor": "#dee2e6",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50012, "version": 1, "versionNonce": 1050012,
    "isDeleted": false, "groupIds": [], "frameId": "comp-team-frame",
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "ellipse",
    "id": "comp-team-dot3",
    "x": 110, "y": 30, "width": 30, "height": 30,
    "strokeColor": "#1e1e1e", "backgroundColor": "#dee2e6",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50013, "version": 1, "versionNonce": 1050013,
    "isDeleted": false, "groupIds": [], "frameId": "comp-team-frame",
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```

---

## External Organization (dashed rectangle)

```json
[
  {
    "type": "rectangle",
    "id": "comp-org",
    "x": 0, "y": 0, "width": 200, "height": 80,
    "strokeColor": "#868e96", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "dashed",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": [{"id": "comp-org-txt", "type": "text"}],
    "seed": 50020, "version": 1, "versionNonce": 1050020,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  },
  {
    "type": "text",
    "id": "comp-org-txt",
    "x": 10, "y": 28, "width": 180, "height": 24,
    "text": "External Partner", "originalText": "External Partner",
    "fontSize": 14, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "comp-org", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#868e96", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "boundElements": null, "seed": 50021, "version": 1, "versionNonce": 1050021,
    "isDeleted": false, "groupIds": [], "frameId": null,
    "updated": 1700000000000, "link": null, "locked": false, "index": null
  }
]
```
