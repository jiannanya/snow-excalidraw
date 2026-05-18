# Flow Primitives

Building blocks for all directional diagrams — pipelines, data flows, process chains, and decision paths.

Use these as atomic components before composing more complex layouts.

---

## Primitive 1: Start Node

Use for the entry point of any flow.

**Shape:** Ellipse with thick border, lighter fill
**Label:** Single verb ("Start", "Request", "User Action", or a specific trigger name)

```json
{
  "id": "start-node",
  "type": "ellipse",
  "x": 80,
  "y": 200,
  "width": 120,
  "height": 60,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#f0f0f0",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100
}
```

---

## Primitive 2: End / Sink Node

Use for the terminal point of any flow.

**Shape:** Ellipse with double border visual effect (use strokeWidth 3)
**Label:** Single noun ("Done", "Output", "Response", or a specific result name)

```json
{
  "id": "end-node",
  "type": "ellipse",
  "x": 1200,
  "y": 200,
  "width": 120,
  "height": 60,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#dee2e6",
  "fillStyle": "solid",
  "strokeWidth": 3,
  "roughness": 1,
  "opacity": 100
}
```

---

## Primitive 3: Process Step

Use for a processing stage, service call, or transformation.

**Shape:** Rectangle with standard styling for the chosen style
**Label:** Verb-noun phrase ("Parse Request", "Apply Rules", "Write to DB")

```json
{
  "id": "process-step",
  "type": "rectangle",
  "x": 280,
  "y": 180,
  "width": 160,
  "height": 80,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100
}
```

---

## Primitive 4: Decision Diamond

Use for a branching condition. Always has exactly 2 outputs: one labeled "Yes/True/Pass" and one "No/False/Fail."

**Shape:** Diamond
**Label:** Question form ("Valid?" "Auth?" "Cache hit?")

```json
{
  "id": "decision-node",
  "type": "diamond",
  "x": 500,
  "y": 160,
  "width": 160,
  "height": 100,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100
}
```

**Arrow placement rule:**
- True / Pass: arrow exits right
- False / Fail / Error: arrow exits bottom and routes downward or loops back left

---

## Primitive 5: Labeled Connector (Arrow)

Use for any directed relationship with a protocol, event, or data name.

```json
{
  "id": "flow-arrow",
  "type": "arrow",
  "x": 440,
  "y": 220,
  "width": 60,
  "height": 0,
  "points": [[0, 0], [60, 0]],
  "startBinding": { "elementId": "process-step", "focus": 0, "gap": 8 },
  "endBinding": { "elementId": "decision-node", "focus": 0, "gap": 8 },
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100,
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

**Label convention:**
- Label the arrow's content type: `JSON`, `gRPC`, `event`, `HTTP 200`
- OR label the condition: `on success`, `if not cached`
- Place label as a text element centered on the arrow midpoint

---

## Primitive 6: Feedback / Loop Arrow

Use when a flow returns to an earlier stage.

**Routing rule:** Bend the arrow below (or above) all intermediate steps to avoid crossing them.

```json
{
  "id": "loop-arrow",
  "type": "arrow",
  "x": 800,
  "y": 260,
  "width": -520,
  "height": 80,
  "points": [[0, 0], [0, 80], [-520, 80], [-520, 0]],
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "strokeStyle": "dashed",
  "opacity": 100,
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

---

## Primitive 7: Parallel Tracks (Fork/Join)

Use when multiple flows run simultaneously.

**Fork:** One arrow enters → splits into two or more arrows out
**Join:** Two or more arrows enter → one arrow out

**Implementation pattern (fork):**
1. Place the fork source shape
2. Draw arrows to each parallel track's first step
3. Space parallel tracks vertically with 100px gaps
4. Place a join shape where tracks reconverge

There is no special Excalidraw shape for fork/join — the visual pattern is the shape layout itself.

---

## Primitive 8: Swimlane Divider

Use when multiple actors or systems run in parallel horizontal lanes.

**Shape:** Horizontal line (type: "line") running full canvas width at the boundary between lanes
**Label:** Left-side text element naming the lane

```json
{
  "id": "swimlane-line-1",
  "type": "line",
  "x": 60,
  "y": 300,
  "width": 1280,
  "height": 0,
  "points": [[0, 0], [1280, 0]],
  "strokeColor": "#adb5bd",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0,
  "strokeStyle": "dashed",
  "opacity": 60
}
```

---

## Primitive 9: Path Marker / Annotation

Use to annotate a specific segment of a flow with a brief observation.

**Shape:** Free-floating text element adjacent to the relevant element or arrow
**Style:** Smaller font (fontSize 14), stroke color lighter than main content

```json
{
  "id": "annotation-text",
  "type": "text",
  "x": 490,
  "y": 280,
  "width": 120,
  "height": 20,
  "text": "⚡ hot path",
  "fontSize": 14,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "#868e96",
  "opacity": 100
}
```

---

## Combining Primitives: Linear Pipeline Template

```
[Start] → [Step A] → [Step B] → [Decision?] → [Step C] → [End]
                                      ↓
                                 [Error/DLQ]
```

- Start: ellipse at (80, 200)
- Step A: rectangle at (280, 180)
- Step B: rectangle at (500, 180)
- Decision: diamond at (720, 160)
- Step C: rectangle at (940, 180)
- End: ellipse at (1160, 200)
- Error: rectangle at (720, 320), stroke red, dashed

See `../catalog/data-flow.md` for full data flow layouts.
