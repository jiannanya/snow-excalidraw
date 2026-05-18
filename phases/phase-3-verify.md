# Phase 3: Verify

**Purpose:** Catch all structural, layout, and quality issues before delivering the diagram.

---

## 3.1 Structural Validation

Run the validator immediately after Phase 2 output:

```bash
cd {skill-root}/scripts
uv run python validate.py "/absolute/path/to/diagram.excalidraw"
```

**Rule:** Phase 4 (Deliver) does not start until the validator exits 0.

Fix every reported error. Common fixes:

| Error | Fix |
|-------|-----|
| Duplicate ID | Rename one element; update all references |
| Missing containerId target | Add the container element, or remove `containerId` |
| Missing boundElements target | Add the referenced element, or remove from `boundElements` |
| Arrow < 2 points | Add a second point to the `points` array |
| Off-canvas element | Move to a valid coordinate within canvas bounds |
| isDeleted: true | Remove the element from the array |

---

## 3.2 Layout Review

After the validator passes, review the layout:

**Spacing check:**
- Every pair of adjacent shapes has ≥ 40px gap
- No shape is within 80px of the canvas edge
- No two shapes overlap

**Flow direction check:**
- The primary flow direction is consistent left→right or top→bottom
- No arrows cross each other without a bend point

**Hierarchy check:**
- The most important element is visually prominent (larger or more isolated)
- Titles are visible and not overlapping content

---

## 3.3 Typography Review

- Every shape has a label ≤ 5 words
- No shape label is empty unless the shape is intentionally unlabeled (e.g., a decorative line)
- Arrow labels are short (≤ 4 words) and visible on the arrow path
- Annotation text is smaller (fontSize ≤ 16) than shape labels (fontSize ≥ 18)

---

## 3.4 Completeness Review

- All components from the Phase 1 intent summary appear in the diagram
- All relationships from the intent summary are represented by arrows
- At least one evidence artifact is present for technical diagrams

---

## 3.5 Style Consistency Review

Spot-check 3 elements from different areas of the diagram:

- [ ] `roughness` matches the chosen style
- [ ] `fontFamily` matches the chosen style
- [ ] `strokeColor` matches the chosen style
- [ ] `backgroundColor` is only non-transparent where semantically needed

If any mismatch is found, correct all elements (not just the sampled ones).

---

## 3.6 Animation Sequence Review (if applicable)

If a `.animseq.json` was produced:

- `order` array must reference only IDs that exist in the `.excalidraw` file
- `duration` values are in milliseconds; minimum per step is 200ms
- Every element that should appear during animation is in the `order` array
- The sequence tells the narrative from beginning to end

---

## 3.7 Revision Loop

If any review check fails:

1. Return to Phase 2 at the point of the failure
2. Fix the issue
3. Overwrite `diagram.excalidraw`
4. Re-run the full Phase 3 verification from step 3.1

**Maximum revisions:** 3 loops. If the diagram still has issues after 3 revision loops, deliver what is available and clearly note remaining issues in the response.

---

## 3.8 Phase 3 Completion Criteria

Phase 3 is complete when all of the following are true:

- [ ] `validate.py` exits 0
- [ ] No layout overlaps
- [ ] Flow direction is consistent
- [ ] All shapes are labeled
- [ ] Style is consistent across all elements
- [ ] All intent components are present

When all criteria are met, proceed to Phase 4.
