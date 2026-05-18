# Excalidraw JSON Specification

Complete reference for the Excalidraw file format used by snow-excalidraw.

---

## File Structure

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null
  },
  "files": {}
}
```

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"excalidraw"` |
| `version` | number | Always `2` |
| `source` | string | Always `"https://excalidraw.com"` |
| `elements` | array | All diagram elements (must be non-empty) |
| `appState` | object | View settings; set `viewBackgroundColor` for dark style |
| `files` | object | Binary assets for image elements; empty for most diagrams |

---

## Element Types

| type | Shape | Common Use |
|------|-------|-----------|
| `rectangle` | Box | Services, screens, steps, data stores |
| `ellipse` | Oval/circle | Entry points, actors, concepts, clusters |
| `diamond` | Rhombus | Decision nodes, gates, branches |
| `arrow` | Arrow | Directed relationships, data flow, transitions |
| `line` | Line | Structural lines, timeline spines, dividers |
| `text` | Text | Free-floating labels, annotations, titles |
| `frame` | Container | Grouping sections or zones |

Advanced types (use sparingly or when explicitly requested):
| `freedraw` | Freehand stroke | Sketch annotations |
| `image` | Raster image | Embedded assets |

---

## Universal Element Properties

All elements share these properties:

| Property | Type | Required | Notes |
|----------|------|----------|-------|
| `id` | string | Yes | Unique across all elements |
| `type` | string | Yes | See element types above |
| `x` | number | Yes | Canvas X position (px) |
| `y` | number | Yes | Canvas Y position (px) |
| `width` | number | Yes | Element width (px) |
| `height` | number | Yes | Element height (px) |
| `angle` | number | Yes | Rotation in radians; use `0` |
| `strokeColor` | string | Yes | Hex color for border/stroke |
| `backgroundColor` | string | Yes | Hex color or `"transparent"` |
| `fillStyle` | string | Yes | `"solid"`, `"hachure"`, `"cross-hatch"` |
| `strokeWidth` | number | Yes | `1`, `2`, or `4` |
| `strokeStyle` | string | Yes | `"solid"`, `"dashed"`, `"dotted"` |
| `roughness` | number | Yes | `0` (smooth), `1` (sketchy) |
| `opacity` | number | Yes | `0–100`; use `100` |
| `seed` | number | Yes | Any unique integer; controls roughness shape |
| `version` | number | Yes | Start at `1` |
| `versionNonce` | number | Yes | Any unique integer |
| `isDeleted` | boolean | Yes | Always `false` |
| `groupIds` | array | Yes | Group membership; `[]` if none |
| `frameId` | string\|null | Yes | Parent frame ID or `null` |
| `boundElements` | array\|null | Yes | Bound text/arrows; `null` if none |
| `updated` | number | Yes | Epoch ms; use `1700000000000` |
| `link` | string\|null | Yes | Hyperlink or `null` |
| `locked` | boolean | Yes | Always `false` |
| `index` | string\|null | Yes | Fractional ordering; use `null` |
| `customData` | object | No | App-specific metadata |

---

## Text Element Extra Properties

| Property | Type | Notes |
|----------|------|-------|
| `text` | string | Displayed text (may be wrapped) |
| `originalText` | string | Source text (unwrapped) |
| `fontSize` | number | Size in px; see style guides |
| `fontFamily` | number | `1`=Virgil, `2`=Helvetica, `3`=Cascadia Code |
| `textAlign` | string | `"left"`, `"center"`, `"right"` |
| `verticalAlign` | string | `"top"`, `"middle"`, `"bottom"` |
| `containerId` | string\|null | ID of parent shape if bound |
| `lineHeight` | number | Use `1.25` |
| `autoResize` | boolean | Always `true` for bound text |

---

## Arrow Element Extra Properties

| Property | Type | Notes |
|----------|------|-------|
| `points` | array | `[[x1,y1], [x2,y2], ...]`; minimum 2 points |
| `startBinding` | object\|null | `{ "elementId": "...", "gap": 5, "focus": 0 }` |
| `endBinding` | object\|null | Same structure as startBinding |
| `startArrowhead` | string\|null | `null`, `"arrow"`, `"bar"`, `"dot"` |
| `endArrowhead` | string\|null | `null`, `"arrow"`, `"bar"`, `"dot"` |
| `elbowed` | boolean | `true` for orthogonal routing |

**Arrow binding rule:** Always bind both ends when the source and target shapes are known. Use `gap: 5` for standard spacing.

---

## Line Element Extra Properties

| Property | Type | Notes |
|----------|------|-------|
| `points` | array | `[[x1,y1], [x2,y2], ...]` |
| `startArrowhead` | string\|null | Always `null` for lines |
| `endArrowhead` | string\|null | Always `null` for lines |

Lines do not bind to shapes. They are structural only.

---

## Frame Element Extra Properties

| Property | Type | Notes |
|----------|------|-------|
| `name` | string | Frame label displayed at top |

Child elements of a frame must have `frameId` set to the frame's `id`.

---

## ID Generation Rules

- Use descriptive IDs when hand-authoring: `"svc-api-gateway"`, `"txt-title"`, `"arrow-login-auth"`
- IDs must be unique across the entire `elements` array
- Bound text IDs: prefix with `"txt-"` followed by the container ID: `"txt-svc-api-gateway"`

---

## Seed and Version

- `seed`: use distinct integers; simple strategy: start at `10001`, increment by 1 per element
- `version`: always `1` for hand-authored elements
- `versionNonce`: always unique; use seed + 1000000 as a simple formula
