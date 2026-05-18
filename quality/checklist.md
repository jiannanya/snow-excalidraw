# Quality Checklist

Run through this checklist before delivering any diagram. Fix every failure before proceeding.

---

## 0. Completeness (Check First)

Before anything else, verify the diagram fully answers the user's question:

- [ ] **Task answered** — the diagram covers everything the user asked for
- [ ] **No missing concepts** — all key nodes, steps, or components are present
- [ ] **No artificial cuts** — elements were not removed just to reduce count

If any of these fail, go back and complete the diagram before continuing.

---

## 1. Validation (Run the Script)

```bash
cd {skill-root}/scripts
uv run python validate.py "/absolute/path/to/diagram.excalidraw"
```

The validator checks:
- Non-empty elements array
- Unique IDs across all elements
- No `isDeleted: true` elements
- All `containerId` references resolve
- All `boundElements` references resolve
- All `startBinding` / `endBinding` references resolve
- No elements at identical coordinates (stacking)
- No off-canvas elements (x < -100 or x > 2000; y < -100 or y > 2000)
- Text content not empty

Fix every reported error. Do not proceed to delivery until the validator exits 0.

---

## 2. Layout

- [ ] **No crowding** — elements have consistent spacing; no overlapping shapes
- [ ] **No orphans** — every element connects to at least one other (exception: title, intentional standalone annotations)
- [ ] **Visual hierarchy** — important elements are visually prominent (larger, more isolated, or bold labels)
- [ ] **Canvas fits content** — no major empty voids and no cut-off elements at canvas edges
- [ ] **Grid discipline** — top-level elements placed at distinct grid cells

---

## 3. Typography

- [ ] **Labels short** — each shape label ≤ 5 words; no sentences or paragraphs inside boxes
- [ ] **Bullets limited** — max 3 short bullets per container; each ≤ 5 words
- [ ] **No duplicate text** — the same explanatory text does not appear in two places
- [ ] **Text fits containers** — no text overflow; containers sized to fit their text
- [ ] **Hierarchy visible** — title font larger than section heading; heading larger than body

---

## 4. Connections

- [ ] **Arrows routed cleanly** — arrows route through whitespace, not through boxes
- [ ] **Arrows bound** — arrows have `startBinding` and `endBinding` when source and target exist
- [ ] **Arrow labels readable** — arrow labels are short and positioned on the arrow path
- [ ] **No ambiguous connections** — the reader can tell which shape each arrow connects to
- [ ] **Bidirectional arrows explained** — if an arrow goes both ways, the label explains why

---

## 5. Style Consistency

- [ ] **Single style used** — all elements follow one style (sketch/blueprint/clean/dark)
- [ ] **Consistent roughness** — all elements use the same roughness value for the chosen style
- [ ] **Consistent font** — all text uses the same fontFamily for the chosen style
- [ ] **Color discipline** — at most one accent color used; semantic colors applied correctly
- [ ] **No decorative fills** — fills are purposeful (grouping, highlight, semantic), not decorative

---

## 6. Content Quality

- [ ] **Concrete content** — real names, event names, protocols, or data types used where relevant
- [ ] **Evidence artifacts present** — for technical diagrams, at least one payload or schema example included
- [ ] **No placeholder boxes** — no empty containers, no "TBD" labels unless explicitly a placeholder
- [ ] **Unique elements** — no two shapes represent the same concept

---

## 7. Delivery

- [ ] **Validator exits 0** — mandatory before calling `open.py`
- [ ] **Source file preserved** — `.excalidraw` file written and retained
- [ ] **Delivery mode correct** — `open.py` called with the mode inferred in Phase 1
- [ ] **Response includes path or link** — the handoff response contains either the launcher path or saved file path

---

## Common Failures and Fixes

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Validator: broken containerId | Text `containerId` doesn't match any shape `id` | Correct the `containerId` to match the shape's exact `id` |
| Validator: broken boundElements | Shape `boundElements` references a non-existent text id | Add the text element, or fix the id in `boundElements` |
| Validator: duplicate id | Two elements share the same `id` | Rename one element's `id` and update all references to it |
| Text overflows box | `width` or `height` too small for the text | Increase container size, or shorten the text |
| Arrow cuts through a box | Arrow uses straight line through content | Add intermediate points to bend the arrow around the box |
| Elements stacked at same coordinates | Two elements at identical (x, y) | Move one to a different grid cell |
| Off-canvas element | x or y coordinate outside reasonable bounds | Recalculate position within 80–1320px (x) and 40–860px (y) |
