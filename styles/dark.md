# Dark Style

A dark-canvas style for technical demos, dashboard diagrams, night-mode presentations, and visual contexts where a dark background improves contrast.

---

## Visual Properties

| Property | Value | Notes |
|----------|-------|-------|
| `strokeColor` | `#dee2e6` | Light gray for standard strokes |
| `backgroundColor` | `transparent` or dark fills | See palette below |
| `fillStyle` | `"solid"` | |
| `strokeWidth` | `2` | Standard |
| `strokeStyle` | `"solid"` | Use `"dashed"` for secondary |
| `roughness` | `0` | Precise; use 1 if user asked for rough dark style |
| `opacity` | `100` | |
| `fontFamily` | `2` (sans) or `3` (mono for tech) | |
| `fontSize` | `14` (body), `18` (heading) | |
| Canvas background | `#1a1b1e` | Very dark gray (near-black) |

**Canvas background must be set in `appState`:**
```json
{
  "appState": {
    "viewBackgroundColor": "#1a1b1e"
  }
}
```

---

## Color Palette

| Role | Color | Hex |
|------|-------|-----|
| Standard stroke | Light gray | `#dee2e6` |
| Secondary stroke | Medium gray | `#868e96` |
| Zone fill | Dark gray | `#2c2e33` |
| Accent (one per diagram) | Cyan / electric blue | `#74c0fc` |
| Success | Soft green | `#69db7c` |
| Warning | Amber | `#ffd43b` |
| Error | Soft red | `#ff6b6b` |
| Text | Off-white | `#f1f3f5` |

---

## Typography

Text in dark style must use light colors to remain readable.

```json
{
  "strokeColor": "#f1f3f5",
  "fontFamily": 2,
  "fontSize": 14
}
```

Arrow labels: `strokeColor: "#dee2e6"`, fontSize: 12

---

## Shape Styling

### Standard node on dark canvas
```json
{
  "strokeColor": "#dee2e6",
  "backgroundColor": "#2c2e33",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0
}
```

### Accent node (one per diagram)
```json
{
  "strokeColor": "#74c0fc",
  "backgroundColor": "#1c3a57",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0
}
```

### Secondary / background node
```json
{
  "strokeColor": "#868e96",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0
}
```

---

## Arrow Style for Dark Canvas
```json
{
  "strokeColor": "#dee2e6",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

---

## Dark Style Dos and Don'ts

| Do | Don't |
|----|-------|
| Set `viewBackgroundColor: "#1a1b1e"` in appState | Use white canvas with dark elements |
| Use light stroke colors for visibility | Use dark strokes on dark canvas |
| Use one bright accent color | Use multiple bright colors |
| Use fills to give nodes body | Leave all shapes transparent on dark canvas |
| Test readability of text | Use low-contrast gray text on gray background |
