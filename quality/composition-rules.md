# Composition Rules

Visual composition principles for Excalidraw diagrams. These rules govern layout, hierarchy, and spacing decisions in Phase 2 (Compose).

---

## Rule 1: One Question Per Diagram

A diagram answers exactly one question. Before composing, state the question explicitly:

> "This diagram answers: how does a user login request travel through the system?"

Everything that doesn't help answer that question is excluded.

---

## Rule 2: Visual Hierarchy

Elements must signal importance through size, placement, and isolation:

| Priority Level | How to Signal |
|---------------|---------------|
| Primary (most important) | Largest shape, placed center-left or center, most isolated |
| Secondary | Medium shape, adjacent to primary |
| Tertiary | Small shape, at edges or grouped |
| Label / annotation | Smallest text, outside shape or on arrow |

**Never use color alone** to indicate importance — color carries semantic meaning, not hierarchy in this system.

---

## Rule 3: Flow Direction

Choose one primary flow direction and stick to it for the whole diagram:

| Flow Direction | When to Use |
|---------------|-------------|
| **Left → Right** | Pipelines, request paths, user journeys, timelines |
| **Top → Bottom** | Org charts, decision trees, dependency graphs |
| **Center → Outward** | Concept webs, radial relationships |
| **Clock (circular)** | Feedback loops, event cycles |

Arrows that fight the primary flow direction signal a revision is needed.

---

## Rule 4: Spacing Discipline

Use these minimum spacing values and do not go below them:

| Context | Minimum Gap |
|---------|------------|
| Between adjacent shapes | 40px |
| Between an arrow and a shape it doesn't connect to | 20px |
| Between a title and the first content shape | 30px |
| Between two separate groups / frames | 60px |
| Between a shape and the canvas edge | 80px |

---

## Rule 5: Grouping Before Connecting

Group related elements before drawing arrows:

1. Identify which elements belong to a logical cluster
2. Place them in a spatial group (or frame)
3. Draw arrows between clusters first
4. Draw arrows within clusters second

This prevents spaghetti and makes the global structure clear.

---

## Rule 6: Frame Scope

Use frames to scope sub-systems, not to decorate:

- A frame represents a zone, layer, or system boundary (e.g., "Frontend", "VPC", "Phase 2")
- Do not create a frame just to add a colored background
- A frame's title should be a short noun phrase (≤ 3 words)
- Frames should not nest more than 2 levels

---

## Rule 7: Arrow Economy

Minimize the number of arrows while preserving meaning:

- If A → B → C are always sequential, prefer drawing them in a line rather than A → B and A → C
- When two arrows go the same direction between the same pair, collapse them into one labeled arrow
- If a concept is referenced by 3+ elements, pull it out as a central node and fan arrows into/out of it

---

## Rule 8: Text Placement

- Shape labels: horizontally and vertically centered inside the shape
- Arrow labels: centered on the arrow path, not at the endpoint
- Floating annotations: placed beside (not inside) the element they describe
- Title: top-left corner at approximately (80, 40), font size ≥ 24

---

## Rule 9: Shape-Type Semantics

Keep shape types semantically consistent across the whole diagram:

| Shape | Semantic Role |
|-------|--------------|
| Rectangle | System component, service, step, module |
| Ellipse | Actor, external system, event, start/end node |
| Diamond | Decision, branching point |
| Arrow | Directed relationship, data flow, control flow |
| Line | Undirected relationship (rare) |
| Frame | System boundary, logical zone, group |
| Text (free) | Title, annotation, label outside a shape |

Do not mix semantics. If a rectangle is a "service," then every service is a rectangle.

---

## Rule 10: The 7 ± 2 Rule

Human working memory holds 7 ± 2 items at a time. A single visual cluster should not have more than 9 direct children. If it does, split into sub-groups or a second diagram.

- A frame with > 9 child elements → split into 2 frames
- A node with > 9 arrows → introduce a hub or aggregation layer
- A diagram with > 25 total elements → consider splitting into overview + detail views

---

## Quick Composition Sequence

1. Write the question the diagram answers
2. Identify primary elements (≤ 7 for a simple diagram)
3. Choose flow direction
4. Place primary elements at grid positions (see `../schema/layout-grid.md`)
5. Add secondary elements and group into frames if needed
6. Draw arrows following primary flow direction
7. Add labels to arrows
8. Add title top-left
9. Review against `anti-patterns.md`
10. Run `validate.py`
