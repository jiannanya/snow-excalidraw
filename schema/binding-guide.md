# Binding Patterns

Reference for correctly binding text to containers and arrows to shapes in Excalidraw JSON.

---

## Text Binding (shape → text)

A shape with a text label must:
1. The **shape** must have `boundElements: [{"id": "<text-id>", "type": "text"}]`
2. The **text** must have `containerId: "<shape-id>"`
3. The **text** must have `autoResize: true`
4. The **text** must have `textAlign: "center"` and `verticalAlign: "middle"` (for centered labels)

### Correct Example

Shape (`rect-svc`):
```json
{
  "id": "rect-svc",
  "type": "rectangle",
  "boundElements": [{"id": "txt-svc", "type": "text"}]
}
```

Text (`txt-svc`):
```json
{
  "id": "txt-svc",
  "type": "text",
  "containerId": "rect-svc",
  "autoResize": true,
  "textAlign": "center",
  "verticalAlign": "middle"
}
```

### Broken Pattern (never do this)

```json
// WRONG: shape has no boundElements
{ "id": "rect-svc", "boundElements": null }

// WRONG: text has no containerId
{ "id": "txt-svc", "containerId": null }

// WRONG: IDs don't match
{ "id": "rect-svc", "boundElements": [{"id": "txt-other", ...}] }
{ "id": "txt-svc", "containerId": "rect-OTHER" }
```

---

## Arrow Binding (arrow → shape)

An arrow must bind to both source and target shapes:
1. The **arrow** must have `startBinding` and `endBinding`
2. Each **shape** must include the arrow in its `boundElements`

### Correct Example

Arrow (`arrow-a-b`):
```json
{
  "id": "arrow-a-b",
  "type": "arrow",
  "startBinding": { "elementId": "rect-a", "gap": 5, "focus": 0 },
  "endBinding":   { "elementId": "rect-b", "gap": 5, "focus": 0 },
  "boundElements": null
}
```

Source shape (`rect-a`):
```json
{
  "id": "rect-a",
  "boundElements": [
    {"id": "txt-a",    "type": "text"},
    {"id": "arrow-a-b", "type": "arrow"}
  ]
}
```

Target shape (`rect-b`):
```json
{
  "id": "rect-b",
  "boundElements": [
    {"id": "txt-b",    "type": "text"},
    {"id": "arrow-a-b", "type": "arrow"}
  ]
}
```

---

## Arrow Label Binding

To add a label to an arrow:
1. Create a `text` element with `containerId: "<arrow-id>"`
2. Add its ID to the arrow's `boundElements`

Arrow with label:
```json
{
  "id": "arrow-a-b",
  "boundElements": [{"id": "txt-arrow-label", "type": "text"}]
}
```

Label text:
```json
{
  "id": "txt-arrow-label",
  "type": "text",
  "containerId": "arrow-a-b",
  "autoResize": true,
  "textAlign": "center",
  "verticalAlign": "middle",
  "fontSize": 12,
  "text": "HTTP POST"
}
```

---

## Frame Binding

Shapes inside a frame must have `frameId: "<frame-id>"`.

Frame element:
```json
{
  "id": "frame-zone",
  "type": "frame",
  "name": "Backend Services"
}
```

Child elements:
```json
{
  "id": "rect-service",
  "frameId": "frame-zone"
}
```

---

## Common Binding Errors (and fixes)

| Error | Symptom | Fix |
|-------|---------|-----|
| `containerId` not matching any shape ID | Validator reports broken reference | Ensure the containerId exactly matches the shape's `id` |
| Shape's `boundElements` missing the text entry | Text floats free; may not render inside shape | Add `{"id": "<text-id>", "type": "text"}` to shape's `boundElements` |
| Arrow bound to shapes that moved off-canvas | Arrow appears disconnected | Re-check coordinate positions of bound shapes |
| Arrow's `startBinding.elementId` does not exist | Validator reports broken reference | Verify the shape ID exists in the elements array |
| Frame's children missing `frameId` | Children appear outside the frame | Add `"frameId": "<frame-id>"` to each child element |
