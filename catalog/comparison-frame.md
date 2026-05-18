# Comparison Frame Diagrams

Use this guide when the goal is to compare options, show trade-offs, contrast before/after states, or evaluate alternatives.

Default style: `clean` (see `../styles/clean.md`)

---

## Canonical Layouts

### Two-Column Comparison (default)
```
┌────────────────┐   ┌────────────────┐
│   Option A     │   │   Option B     │
│                │   │                │
│  • Feature 1   │   │  • Feature 1   │
│  • Feature 2   │   │  • Feature 2   │
│  • Feature 3   │   │  • Feature 3   │
└────────────────┘   └────────────────┘
```
Use for: A vs B comparisons, option evaluation, technology trade-offs.

### Before / After
```
┌──── BEFORE ────┐   ┌──── AFTER ─────┐
│                │ → │                │
│  [Old state]   │   │  [New state]   │
└────────────────┘   └────────────────┘
```
Use for: refactoring, migration plans, process improvements, UX redesigns.

### Multi-Column Matrix
```
         | Feature A | Feature B | Feature C |
Option 1 |    ✓      |    ✗      |    ✓      |
Option 2 |    ✗      |    ✓      |    ✓      |
Option 3 |    ✓      |    ✓      |    ✗      |
```
Use for: feature comparison tables, decision matrices.

### Spectrum / Scale
```
[Fast ◄──────────────────────► Slow]
  DB Cache    DB Primary    Network Disk
```
Use for: trade-off spectrums, performance axes, cost vs. quality scales.

---

## Required Elements

1. **Clear column/side labels** — what each option, time period, or axis represents
2. **Same criteria on each side** — compare apples to apples; list the same attributes for each option
3. **Visible distinction** — the reader must immediately see which side is which
4. **A verdict or recommendation** (optional but valuable) — float a `text` label indicating the recommended choice or conclusion

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Column panel | `rectangle` (tall) | One per option |
| Column header | `text` (bold, large) inside top of panel | Name of option |
| Attribute row | `text` (bullet format) | Same for each panel |
| Divider | `line` (vertical) | Separates columns |
| Before arrow | `arrow` (horizontal) | Points from before to after panel |
| Verdict callout | `text` (floating) or `ellipse` with label | "Recommended" or "Winner" callout |
| Check / Cross | `text` with ✓ or ✗ | For feature matrices |
| Spectrum spine | `line` (horizontal) | Labeled at both ends |
| Spectrum marker | `ellipse` (small, filled) | One per item on the spectrum |

---

## Criteria Parity Rule

Every comparison must use the **same criteria** on each side:

- If Option A lists "Speed", "Cost", "Complexity" → Option B must list the same three
- Never add a criterion to one option that doesn't appear on the other
- If a criterion does not apply, mark it explicitly (e.g., "N/A")

---

## Anti-Patterns

- One side has more items than the other (asymmetric comparison)
- Unlabeled columns (the reader cannot tell what is being compared)
- Comparison of items that are not actually comparable at the same level of abstraction
- Before/after without a visible transformation arrow between them
- Including too many criteria (more than 7) that dilute the key trade-off
