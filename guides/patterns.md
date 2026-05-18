# Visual Patterns Library

Reusable composition patterns for building clear, consistent diagrams.

---

## Pattern Index

| # | Pattern | Use case |
|---|---------|----------|
| 1 | Linear Chain | Process steps, pipelines |
| 2 | Hub-and-Spoke | Centralised service / concept |
| 3 | Layered Stack | Architectural tiers |
| 4 | Grid Matrix | Comparison, feature matrix |
| 5 | Tree Hierarchy | Org charts, taxonomies |
| 6 | Loop / Cycle | Feedback, recurring workflows |
| 7 | Fan-out / Broadcast | One source → many targets |
| 8 | Swim Lane | Cross-team or cross-system flows |
| 9 | Timeline Strip | Chronological events |
| 10 | Decision Diamond | Branch / decision point |

---

## Pattern 1 — Linear Chain

**Shape:** Row of rectangles connected by horizontal arrows.

```
[A] ──► [B] ──► [C] ──► [D]
```

- Y fixed for all shapes (same row)
- X increments by (shape width + gap), e.g. `x = 80 + n * 300`
- Use `strokeWidth: 2` arrows with `endArrowhead: "arrow"`

Best for: data pipeline, processing stages, onboarding steps.

---

## Pattern 2 — Hub-and-Spoke

**Shape:** Central shape surrounded by 4–8 satellite shapes with arrows radiating out.

Place hub at canvas centre (`x ≈ 850, y ≈ 480`). Place spokes at:

| Position | x offset | y offset |
|----------|----------|----------|
| Top | 0 | -200 |
| Top-right | +200 | -140 |
| Right | +280 | 0 |
| Bottom-right | +200 | +140 |
| Bottom | 0 | +200 |
| Bottom-left | -200 | +140 |
| Left | -280 | 0 |
| Top-left | -200 | -140 |

Best for: API gateway, message broker, central concept map.

---

## Pattern 3 — Layered Stack

**Shape:** Horizontally-wide rectangles stacked vertically, each labelled as a tier.

```
┌──────────────────────────────────┐  Presentation
├──────────────────────────────────┤  Application
├──────────────────────────────────┤  Data
└──────────────────────────────────┘  Infrastructure
```

- Shared width: 1400 px, starting x = 200
- Heights: 100 px each, gap 8 px
- Colour: top tier lightest, bottom tier darkest

Best for: OSI model, software stack, architecture layers.

---

## Pattern 4 — Grid Matrix

**Shape:** N × M grid of shapes with row and column headers.

| Cell position | Formula |
|---------------|---------|
| `x` | `header_w + col * (cell_w + gap)` |
| `y` | `header_h + row * (cell_h + gap)` |

Use `frameId` to group each row, or `groupIds` for column grouping.

Best for: feature comparison table, risk matrix, prioritisation grid.

---

## Pattern 5 — Tree Hierarchy

**Shape:** Root at top, children below via vertical+horizontal arrows.

```
           [Root]
          /       \
      [Child A]  [Child B]
      /   \
 [Leaf 1] [Leaf 2]
```

- Root at `y = 80`
- Each level adds `y += 160`
- Sibling spacing: `(canvas_width / sibling_count)` per level

Best for: org chart, file system tree, decision tree.

---

## Pattern 6 — Loop / Cycle

**Shape:** Shapes arranged in a ring; arrows form a closed cycle.

For a 4-node cycle, place nodes at the corners of a square:

```
[A] ──► [B]
 ▲       │
 │       ▼
[D] ◄── [C]
```

Centre the square on the canvas. Use elbow arrows for clean routing.

Best for: CI/CD pipeline, feedback loop, PDCA cycle.

---

## Pattern 7 — Fan-out / Broadcast

**Shape:** One source shape → multiple target shapes; each with its own arrow.

```
         ┌─► [Target 1]
[Source] ├─► [Target 2]
         └─► [Target 3]
```

Use `focus` values (-0.4, 0, 0.4) on `startBinding` to spread arrow origins on the source edge.

Best for: load balancer, event bus, notification dispatch.

---

## Pattern 8 — Swim Lane

**Shape:** Horizontal bands (rectangles) labelled per actor, with process arrows flowing left-to-right within each lane.

| Lane | Y start | Height |
|------|---------|--------|
| Lane 1 | 80 | 200 |
| Lane 2 | 280 | 200 |
| Lane 3 | 480 | 200 |

Lane label: rotate text 90° (`angle: -1.5708`) in a narrow left-margin column.

Best for: cross-team workflows, multi-system interaction flows.

---

## Pattern 9 — Timeline Strip

**Shape:** Horizontal spine line with vertical tick marks and event labels above/below.

```
──────●───────●───────●───────●──────
    Q1 2024  Q2 2024  Q3 2024  Q4 2024
    [Event A]         [Event B]
```

Tick marks: short vertical lines at milestone x positions.
Events above spine: `y = spine_y - label_height - 12`
Events below spine: `y = spine_y + 12`

Alternate above/below to avoid label overlap.

Best for: product roadmap, project timeline, sprint calendar.

---

## Pattern 10 — Decision Diamond

**Shape:** Diamond (rotated square) for branch points; outgoing arrows labelled Yes/No or condition names.

```json
{
  "type": "diamond",
  "id": "dec-1",
  "x": 700, "y": 300,
  "width": 200, "height": 120,
  "boundElements": [{"id": "lbl-dec-1", "type": "text"}]
}
```

Arrow labels:
- `"Yes"` or `"true"` → downward continuation
- `"No"` or `"false"` → right or left branch

Position labels 8 px off the arrow line using free-floating text.

Best for: flowcharts, conditional logic, troubleshooting trees.
