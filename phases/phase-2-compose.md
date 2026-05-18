# Phase 2: Compose

**Purpose:** Produce valid, complete Excalidraw JSON from the intent summary built in Phase 1.

---

## 2.1 Pre-Composition Checklist

Before writing any JSON, confirm:

- [ ] Intent summary from Phase 1 is complete (type, style, components, relationships)
- [ ] Correct catalog file loaded (`../catalog/<type>.md`)
- [ ] Correct style file loaded (`../styles/<style>.md`)
- [ ] Layout template selected from the catalog file

If any is missing, return to Phase 1 and resolve before proceeding.

---

## 2.2 Layout Selection

Each catalog file defines multiple layout templates. Select based on complexity:

| Component Count | Default Layout Strategy |
|----------------|------------------------|
| 2–4 components | Simplest layout (linear or radial) |
| 5–8 components | Standard layout (pipeline, top-down, or clustered) |
| 9–14 components | Multi-zone layout (frame-based grouping) |
| 15+ components | Split into overview + 2 detail diagrams |

---

## 2.3 Grid Placement

Use the canvas grid from `../schema/layout-grid.md`:

1. Assign each major component to a grid cell
2. Write down the (x, y) coordinate for each component
3. Check that no two components share the same cell
4. Add 40px minimum gap between adjacent shapes

**Grid quick reference:**
```
col:  1=80   2=300  3=520  4=740  5=960  6=1180
row:  1=40   2=160  3=280  4=400  5=520  6=640  7=760
```

---

## 2.4 Element Construction Order

Build elements in this order to avoid broken references:

1. **Frames** — must exist before any element references `frameId`
2. **Shapes** (rectangles, ellipses, diamonds) — must exist before text elements reference `containerId`
3. **Text elements** — bound text must be created after their container shape
4. **Arrows** — created after all shapes they connect; reference `startBinding.elementId` and `endBinding.elementId`
5. **Annotations** (free-floating text) — created last, no binding required

**autoResize rule (mandatory):** Every text element whose `containerId` is non-null **must** include `"autoResize": true`. Omitting this causes text to be clipped or misaligned inside its container.

```json
// CORRECT — bound text inside a rectangle
{
  "type": "text",
  "containerId": "rect-1",
  "autoResize": true,
  "textAlign": "center",
  "verticalAlign": "middle"
}

// WRONG — bound text without autoResize
{
  "type": "text",
  "containerId": "rect-1"
  // missing autoResize!
}
```

---

## 2.5 Style Application

Apply style properties from `../styles/<chosen-style>.md` to every element:

| Style | roughness | fontFamily | strokeColor |
|-------|-----------|------------|-------------|
| sketch | 1 | 1 (Virgil) | #1e1e1e |
| blueprint | 0 | 3 (Cascadia) | #1864ab |
| clean | 0 | 2 (Helvetica) | #212529 |
| dark | 0 | 2 (Helvetica) | #dee2e6 |

- Set these values on every element, not just the first few
- For dark style, also set `appState.viewBackgroundColor: "#1a1b1e"`

---

## 2.6 Component Library Usage

Before creating custom shapes, check available components:

| What you need | Component file |
|---------------|---------------|
| Server, node, load balancer, cloud zone, Kubernetes pod | `../components/servers-and-infra.md` |
| Browser chrome, mobile screen, desktop window | `../components/interfaces.md` |
| Database, cache, message queue, object store | `../components/data-stores.md` |
| Person, team, external org | `../components/actors.md` |
| Start/end node, decision, pipeline arrow, swimlane | `../components/flow-primitives.md` |
| Warning badge, success tick, error marker, annotation | `../components/callout-kit.md` |

Copy the JSON template from the component file and update id, x, y, and label.

---

## 2.7 ID Convention

All element IDs must be unique within the diagram. Use this convention:

```
<type>-<slug>-<sequence>
```

Examples:
- `rect-api-gateway-1`
- `text-api-gateway-label-1`
- `arrow-browser-to-api-1`
- `frame-frontend-zone-1`
- `ellipse-user-actor-1`

IDs must be strings, no spaces, no dots.

---

## 2.8 Binding Verification During Composition

After writing each arrow, verify:
- `startBinding.elementId` → shape exists in elements before the arrow
- `endBinding.elementId` → shape exists in elements before the arrow

After writing each text element, verify:
- If `containerId` is set → the container shape exists
- The container shape's `boundElements` includes this text element's id

Use `../schema/binding-guide.md` for the complete binding pattern.

---

## 2.9 Evidence Artifacts

For System Design and Data Flow diagrams, include at least one evidence artifact:
- JSON payload example (as a free text element near the relevant component)
- Schema snippet
- Timing or metric label (`p99: 12ms`, `throughput: 5k msg/s`)

---

## 2.10 Title Block

Every diagram includes a title. Place it at approximately (80, 20):

```json
{
  "id": "title-text",
  "type": "text",
  "x": 80,
  "y": 20,
  "width": 600,
  "height": 40,
  "text": "Diagram Title",
  "fontSize": 28,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "#1e1e1e",
  "opacity": 100
}
```

---

## 2.11 Full File Structure

Wrap all elements in the required Excalidraw file envelope:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [ ...all elements... ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

For dark style: `"viewBackgroundColor": "#1a1b1e"`

---

## 2.12 Output Commitment

At the end of Phase 2, produce:

1. The complete `.excalidraw` JSON (written to `diagram.excalidraw`)
2. Optionally, a `.animseq.json` if animation was planned
3. A brief text confirmation: `"diagram.excalidraw written — N elements"`

Then immediately proceed to Phase 3 (Verify).
