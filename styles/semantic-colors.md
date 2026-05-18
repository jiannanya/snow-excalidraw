# Semantic Color Reference

Use these colors consistently across all styles. Colors are assigned by **semantic meaning**, not decoration.

---

## Universal Semantic Colors

These work across all four styles (sketch, blueprint, clean, dark):

| Semantic Role | Light Styles Hex | Dark Style Hex | Usage |
|---------------|-----------------|----------------|-------|
| Primary / neutral | `#1e1e1e` | `#dee2e6` | Default strokes and text |
| Accent / highlight | `#1971c2` | `#74c0fc` | Most important element only |
| Success / positive | `#2f9e44` | `#69db7c` | Confirmed state, correct path |
| Warning / caution | `#e67700` | `#ffd43b` | Risk, retry, caution |
| Error / failure | `#c92a2a` | `#ff6b6b` | Errors, dead ends, failures |
| Secondary / inactive | `#868e96` | `#868e96` | Background, less-important elements |
| External / unknown | `#5f3dc4` | `#b197fc` | Third-party systems, external actors |

---

## Fill Colors by Semantic Role

| Role | Light Style Fill | Dark Style Fill |
|------|-----------------|----------------|
| Neutral / background | `#f8f9fa` | `#2c2e33` |
| Accent zone | `#e7f5ff` | `#1c3a57` |
| Success zone | `#ebfbee` | `#1a3824` |
| Warning zone | `#fff9db` | `#3b2e00` |
| Error zone | `#fff5f5` | `#3b0f0f` |
| External zone | `#f3f0ff` | `#2a1f4a` |

---

## Usage Rules

1. **One accent color per diagram** — pick the element that matters most and apply accent to it only
2. **Semantic consistency** — never use red for anything other than errors/failures; never use green for anything other than success/positive
3. **Fill = grouping, not decoration** — fills are for highlighting zones or drawing attention; not for visual variety
4. **No rainbow diagrams** — if you find yourself using more than 3 colors, remove the least important ones

---

## Color Application Examples

### System Design (blueprint style)
- Services: blue stroke `#1864ab`
- Error path: red stroke `#c92a2a`, dashed
- External system: gray stroke `#868e96`, dashed

### Product Journey (sketch style)
- Main path: black `#1e1e1e`
- Success end state: green fill `#ebfbee`
- Error / dead end: red fill `#fff5f5`

### Wireframe Kit (sketch style, minimal color)
- CTA button: accent blue `#1971c2` fill, white text
- Warning message: error fill `#fff5f5`
- Everything else: monochrome

---

## What NOT to Do

- Do not assign different colors to different services just for variety
- Do not use yellow for anything other than warning/caution
- Do not use purple for anything other than external/third-party systems
- Do not mix light and dark palette in the same diagram
