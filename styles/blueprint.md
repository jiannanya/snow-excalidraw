# Blueprint Style

A technical, structured style for architecture and infrastructure diagrams. Crisp lines, monospace annotations, and a blue-tinted palette for a technical "specification" aesthetic.

---

## Visual Properties

| Property | Value | Notes |
|----------|-------|-------|
| `strokeColor` | `#1864ab` | Dark blue for primary strokes |
| `backgroundColor` | `transparent` or `#e7f5ff` | Light blue wash for primary zones |
| `fillStyle` | `"solid"` | Clean, no hatching |
| `strokeWidth` | `2` | Standard; use `1` for secondary |
| `strokeStyle` | `"solid"` | Use `"dashed"` for optional/external elements |
| `roughness` | `0` | Always 0 for blueprint style (smooth, precise) |
| `opacity` | `100` | |
| `fontFamily` | `3` | Cascadia Code / monospace for technical labels |
| `fontSize` | `14` (body), `16` (heading) | Smaller type for denser technical detail |
| Canvas background | `#f8f9fa` | Off-white / light gray |

---

## Color Palette

Blueprint style uses a restricted blue palette with one red accent for errors/warnings.

| Role | Color | Hex |
|------|-------|-----|
| Primary service / component | Blue stroke | `#1864ab` |
| Zone / cluster fill | Light blue | `#e7f5ff` |
| External / third-party | Gray | `#868e96` |
| Error / failure path | Red | `#c92a2a` |
| Data store | Darker blue | `#1c7ed6` |
| Arrow / connector | Dark blue | `#1864ab` |
| Evidence artifact bg | Near-white | `#f1f3f5` |

---

## Typography

Blueprint style uses monospace (fontFamily: 3) for precision.

| Text Role | fontSize | fontFamily |
|-----------|----------|------------|
| System / service name | 14 | 3 (monospace) |
| Protocol label on arrow | 12 | 3 (monospace) |
| Section header | 16 | 3 (monospace) |
| Annotation / note | 12 | 3 (monospace) |

---

## Arrow Style

Arrows in blueprint style represent data/request flow. Always label with protocol or method.

```json
{
  "strokeColor": "#1864ab",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

Failure/fallback arrows:
```json
{
  "strokeColor": "#c92a2a",
  "strokeWidth": 1,
  "strokeStyle": "dashed",
  "roughness": 0
}
```

---

## Evidence Artifact Panel

For technical diagrams, include JSON/payload examples in a styled panel:

```json
{
  "type": "rectangle",
  "strokeColor": "#868e96",
  "backgroundColor": "#f1f3f5",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "dashed",
  "roughness": 0
}
```

Text inside: fontFamily: 3, fontSize: 12, monospace.

---

## Blueprint Style Dos and Don'ts

| Do | Don't |
|----|-------|
| Use roughness: 0 for precision | Use roughness: 1 (that's sketch style) |
| Label every arrow with protocol | Leave arrows unlabeled |
| Use monospace font for all labels | Use Virgil/handwriting font |
| Use blue color hierarchy | Use more than 3 colors |
| Include evidence artifacts | Create abstract-only diagrams |
