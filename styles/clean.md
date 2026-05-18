# Clean Style

A minimal, sharp, presentation-ready style. Smooth lines, geometric shapes, and a restrained color palette for polished deliverables.

---

## Visual Properties

| Property | Value | Notes |
|----------|-------|-------|
| `strokeColor` | `#212529` | Near-black |
| `backgroundColor` | `transparent` or specific fill | Fills permitted per semantic palette |
| `fillStyle` | `"solid"` | Clean, no texture |
| `strokeWidth` | `1.5` or `2` | Use 1 for borders, 2 for main flow |
| `strokeStyle` | `"solid"` | Use `"dashed"` for secondary/inactive |
| `roughness` | `0` | Always 0 for clean style |
| `opacity` | `100` | |
| `fontFamily` | `2` | Helvetica / sans-serif |
| `fontSize` | `14` (body), `18` (heading) | |
| Canvas background | `#ffffff` | Pure white |

---

## Color Palette

Clean style uses a minimal neutral palette with optional one-color accent.

| Role | Color | Hex |
|------|-------|-----|
| Primary text / strokes | Near-black | `#212529` |
| Secondary element | Medium gray | `#868e96` |
| Subtle fill | Light gray | `#f8f9fa` |
| Accent (optional) | Brand blue | `#1971c2` |
| Positive / success | Green | `#2f9e44` |
| Warning / negative | Red | `#c92a2a` |

Use at most **one accent color** per diagram. Use accent only for the most important element (primary CTA, key node, critical path).

---

## Typography

Clean style uses Helvetica (fontFamily: 2) for a modern feel.

| Text Role | fontSize | fontWeight | Notes |
|-----------|----------|------------|-------|
| Title | 22 | bold (use larger strokeWidth) | Top of diagram |
| Section heading | 18 | standard | Group labels |
| Body / node label | 14 | standard | Shape labels |
| Annotation | 12 | standard | Supporting notes |
| Arrow label | 11 | standard | Inline with arrows |

---

## Shape Styling

### Primary nodes
```json
{
  "strokeColor": "#212529",
  "backgroundColor": "#f8f9fa",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0
}
```

### Secondary / background nodes
```json
{
  "strokeColor": "#868e96",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0
}
```

### Accent / highlight node (one per diagram)
```json
{
  "strokeColor": "#1971c2",
  "backgroundColor": "#e7f5ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0
}
```

---

## Clean Style Dos and Don'ts

| Do | Don't |
|----|-------|
| Use roughness: 0 for crispness | Use roughness: 1 |
| Use one accent color max | Use multiple colors |
| Use sans-serif font (fontFamily: 2) | Use Virgil/handwriting |
| Apply fills purposefully | Leave all shapes transparent |
| Keep generous whitespace | Pack elements tightly |
| Bold the title with larger font | Make all text the same size |
