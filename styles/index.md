# Style System Index

Snow-Excalidraw supports four visual styles. Each diagram type has a recommended default style. The user can override by requesting a different style in their prompt.

---

## Style Summary

| Style | File | Aesthetic | Best For |
|-------|------|-----------|----------|
| `sketch` | `sketch.md` | Rough, hand-drawn, organic | Teaching, brainstorming, wireframes, narrative |
| `blueprint` | `blueprint.md` | Technical, precise, structured | Architecture, infrastructure, data pipelines |
| `clean` | `clean.md` | Minimal, sharp, presentation-ready | Org charts, timelines, comparisons, polished decks |
| `dark` | `dark.md` | Dark canvas, light strokes | Dashboard backgrounds, tech demos, night mode |

---

## Style Selection Logic

1. **Check the catalog entry** — each diagram type specifies a default style
2. **Check user signals** — words like "rough", "sketch", "technical", "clean", "dark", "presentation" override the default
3. **Check context** — if the user is making a document/deck, prefer `clean`; if exploring ideas, prefer `sketch`

---

## Style Override Keywords

| User Says | Style to Use |
|-----------|-------------|
| "rough", "sketch", "hand-drawn", "informal", "doodle" | `sketch` |
| "technical", "blueprint", "spec", "infra", "architecture" | `blueprint` |
| "clean", "minimal", "presentation", "polished", "slides" | `clean` |
| "dark", "dark mode", "dark theme", "night" | `dark` |

---

## Color Philosophy

- `sketch`: monochrome (black on white); restrained color only for specific callouts
- `blueprint`: blue-tinted strokes on white; dark blue for emphasis
- `clean`: monochrome or minimal 2-color palette (one neutral, one accent)
- `dark`: light strokes on dark canvas; one accent color permitted

See `semantic-colors.md` for the approved color palette used across all styles.
