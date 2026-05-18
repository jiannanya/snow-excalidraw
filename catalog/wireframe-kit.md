# Wireframe Kit Diagrams

Use this guide when the goal is to sketch UI layouts, page mockups, dashboard wireframes, or application screen designs.

Default style: `sketch` (see `../styles/sketch.md`). Use `clean` style when the user asks for a presentation-quality wireframe.

---

## Canonical Layouts

### Landing Page (top-to-bottom)
```
[Nav Bar]
[Hero Section]
[Feature Grid]
[Social Proof]
[Pricing]
[CTA Footer]
```
Use for: landing pages, product pages, marketing pages.

### Dashboard (grid-based)
```
[Nav Sidebar] | [Header / Search]
              | [KPI Cards Row]
              | [Main Chart]    [Secondary Chart]
              | [Data Table]
```
Use for: admin dashboards, analytics pages, internal tools.

### Mobile Screen (portrait)
```
[Status Bar]
[Navigation Header]
[Content Area]
   [Card 1]
   [Card 2]
[Bottom Nav Bar]
```
Use for: mobile app screens, responsive layouts, app flows.

### Form / Checkout
```
[Progress Bar: Step 1 / 2 / 3]
[Form Fields]
  [Label] [Input Field]
  [Label] [Input Field]
[CTA Button]
```
Use for: checkout flows, signup forms, multi-step wizards.

---

## Required Elements

1. **Page boundary** — the outer container representing the screen or viewport
2. **Navigation element** — header, nav bar, or sidebar
3. **Primary content area** — the main body of the page
4. **At least one CTA** — the primary action the user should take
5. **Typographic hierarchy** — show heading vs body vs label distinction through size

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Page / Viewport | `rectangle` (large, outer container) | The screen boundary |
| Navigation Bar | `rectangle` (thin, full-width at top) | Use label "Nav" or actual nav items |
| Hero Section | `rectangle` (large, prominent) | First content section |
| Button / CTA | `rectangle` (small, rounded-ish) | Label with button text |
| Input Field | `rectangle` (thin, wide) | Label beside it, not inside |
| Image Placeholder | `rectangle` with "×" or "IMG" label | Never use real image paths |
| Icon Placeholder | `ellipse` (small) or `rectangle` (small square) | Label "icon" |
| Text Block | `text` (wavy lines implied by Virgil font) | Represent body copy with short Lorem-like label |
| Card | `rectangle` | Rounded look; group with `frame` if multiple cards |
| Divider | `line` (horizontal) | Separates page sections |
| Footer | `rectangle` (thin, full-width at bottom) | Label "Footer" |

---

## Fidelity Levels

| Fidelity | What to Show | When to Use |
|----------|-------------|-------------|
| Low (default sketch) | Layout structure, section names only | Early ideation, layout exploration |
| Medium (clean style) | Component shapes, rough labels | Stakeholder review, scope planning |
| High (annotated) | All components labeled, notes on interactions | Handoff to engineers or designers |

**Default is low fidelity.** Increase only when the user explicitly asks for "detailed" or "presentation-ready" wireframes.

---

## Color Rule for Wireframes

Wireframes use monochrome by default. Allow one accent color only when:
- User asks for "color" or "hi-fi" wireframe
- A CTA or warning state must be visually distinguished

Use semantic color from `../styles/semantic-colors.md`:
- Primary action: `#1971c2` (blue)
- Warning / error: `#c92a2a` (red)
- Success: `#2f9e44` (green)

---

## Anti-Patterns

- Real content in wireframes (actual product copy, real data)
- Drawn UI components too detailed (wireframes are structure, not design)
- No visible CTA
- All sections the same size (no visual hierarchy)
- Combining wireframe with flow diagram arrows inside the screen content
