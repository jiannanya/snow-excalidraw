# Animation Sequence Specification

Reference for writing `.animseq.json` files that control how diagrams animate using `excalidraw-animate`.

---

## What is `.animseq.json`?

A companion file to the `.excalidraw` source that defines the order and timing of element animations. Each Excalidraw element type has a natural animation behavior:

| Element Type | Animation Behavior |
|---|---|
| `rectangle` | Border draws as polygon → fill fades in |
| `ellipse` | Outline traces oval → fill fades in |
| `diamond` | Same as rectangle |
| `arrow` | Shaft draws first (60%) → arrowhead appears (40%) |
| `line` | Draws along its path start to end |
| `text` | Reveals left-to-right with sliding clip |
| `frame` | Border draws, then contents animate within |
| `image` | Fade-in only |

---

## File Format

```json
{
  "startMs": 500,
  "defaultDuration": 500,
  "elements": [
    { "id": "element-id", "order": 1, "duration": 300 },
    { "id": "another-id", "order": 1, "duration": 300 },
    { "id": "arrow-id",   "order": 2, "duration": 500 }
  ]
}
```

| Field | Default | Description |
|---|---|---|
| `startMs` | `0` | Delay before the first element starts |
| `defaultDuration` | `500` | Duration for elements not listed in `elements[]` |
| `elements[].id` | — | Must match an element `id` in the `.excalidraw` file |
| `elements[].order` | — | Lower = animates first; same order = simultaneous |
| `elements[].duration` | `defaultDuration` | Duration in milliseconds for this element |

---

## Duration Reference

| Element | Recommended Duration |
|---|---|
| Title text | 200–300ms |
| Section heading text | 300ms |
| Rectangle / ellipse / diamond | 400–600ms |
| Arrow | 400–700ms |
| Line (short) | 200–300ms |
| Line (long, spine) | 400–600ms |
| Complex frame with children | 800–1200ms total |

**Total animation time target:**
- Simple diagram (5–8 elements): 6–12 seconds
- Medium diagram (9–15 elements): 10–20 seconds
- Complex diagram (16+ elements): 15–30 seconds

---

## Order Rules

1. **Title animates first** → `order: 1`
2. **Container before its content** → frame/box at `order: N`, text at `order: N` (same, simultaneous) or `N+1`
3. **Arrows after their source and target** → never animate an arrow before the shapes it connects
4. **Group related elements at same order** → sibling services appear together, not one by one
5. **Main path before branches** → primary flow animates before error/alternative paths

---

## Narrative Sequencing Patterns

### Linear Story (left-to-right)
```json
{ "id": "title", "order": 1, "duration": 300 },
{ "id": "node-1", "order": 2, "duration": 500 },
{ "id": "txt-1",  "order": 2, "duration": 300 },
{ "id": "arrow-1-2", "order": 3, "duration": 400 },
{ "id": "node-2", "order": 4, "duration": 500 },
{ "id": "txt-2",  "order": 4, "duration": 300 }
```

### Fan-Out Reveal
```json
{ "id": "title",    "order": 1, "duration": 300 },
{ "id": "center",   "order": 2, "duration": 600 },
{ "id": "center-txt", "order": 2, "duration": 400 },
{ "id": "arrow-to-a", "order": 3, "duration": 400 },
{ "id": "arrow-to-b", "order": 3, "duration": 400 },
{ "id": "arrow-to-c", "order": 3, "duration": 400 },
{ "id": "node-a",  "order": 4, "duration": 500 },
{ "id": "node-b",  "order": 4, "duration": 500 },
{ "id": "node-c",  "order": 4, "duration": 500 }
```

### Layer-by-Layer (top-to-bottom stacks)
```json
{ "id": "title",   "order": 1, "duration": 300 },
{ "id": "layer-1", "order": 2, "duration": 600 },
{ "id": "arrow-1", "order": 3, "duration": 300 },
{ "id": "layer-2", "order": 4, "duration": 600 },
{ "id": "arrow-2", "order": 5, "duration": 300 },
{ "id": "layer-3", "order": 6, "duration": 600 }
```

### Comparison Reveal (parallel columns)
```json
{ "id": "title",      "order": 1, "duration": 300 },
{ "id": "col-a-header", "order": 2, "duration": 400 },
{ "id": "col-b-header", "order": 2, "duration": 400 },
{ "id": "col-a-row1",   "order": 3, "duration": 300 },
{ "id": "col-b-row1",   "order": 3, "duration": 300 },
{ "id": "col-a-row2",   "order": 4, "duration": 300 },
{ "id": "col-b-row2",   "order": 4, "duration": 300 }
```

---

## File Naming

Save the animation sequence file as:
```
diagram.animseq.json
```

Place it in the same directory as `diagram.excalidraw`.

The `open.py` script will automatically detect and use it when `--mode animate` is specified.
