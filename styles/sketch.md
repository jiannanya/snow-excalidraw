# Sketch Style

The default style for most diagrams. Rough, hand-drawn, and organic. Uses the Virgil handwriting font for a sketch aesthetic.

---

## Visual Properties

| Property | Value | Notes |
|----------|-------|-------|
| `strokeColor` | `#1e1e1e` | Near-black for all strokes |
| `backgroundColor` | `transparent` or `#ffffff` | Most shapes use transparent fill |
| `fillStyle` | `"hachure"` | Hatching gives hand-drawn texture; use "solid" only for callouts |
| `strokeWidth` | `2` | Standard; use `1` for minor/secondary elements |
| `strokeStyle` | `"solid"` | Use `"dashed"` for secondary/optional elements |
| `roughness` | `1` | Always 1 for sketch style |
| `opacity` | `100` | |
| `fontFamily` | `1` | Virgil handwritten font |
| `fontSize` | `16` (body), `20` (heading) | |
| Canvas background | `#ffffff` | White canvas |

---

## Fill Usage

Sketch style is monochrome by default. Fill is allowed only for:

| Use Case | Fill Value |
|----------|-----------|
| Emphasis callout | `#ffe066` (light yellow) |
| Warning / error | `#ffa8a8` (light red) |
| Success / positive | `#b2f2bb` (light green) |
| All other shapes | `transparent` |

Use at most **one accent fill per diagram**. Do not use fills for decoration.

---

## Typography

All text uses Virgil (fontFamily: 1) in sketch style.

| Text Role | fontSize | Notes |
|-----------|----------|-------|
| Title / heading | 24 | First label in the diagram |
| Section heading | 20 | Sub-group labels |
| Body label | 16 | Shape labels, node text |
| Annotation | 14 | Floating notes, callouts |
| Small label | 12 | Arrow labels, minor annotations |

---

## Arrow Style

```json
{
  "strokeColor": "#1e1e1e",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

- Bidirectional arrows: `startArrowhead: "arrow"`, `endArrowhead: "arrow"`
- Structural lines (non-directional): use `line` type instead of `arrow`

---

## Sketch Style Dos and Don'ts

| Do | Don't |
|----|-------|
| Use hachure fill for emphasis shapes | Fill every shape |
| Keep strokes rough (roughness: 1) | Use roughness: 0 (that's clean style) |
| Mix shape types for visual variety | Use all rectangles |
| Use Virgil font for organic feel | Switch to system/sans-serif font |
| Use whitespace generously | Pack elements tightly |
