# Concept Web Diagrams

Use this guide when the goal is to explore, map, or visualize relationships between ideas, topics, or concepts — mind maps, concept maps, topic clusters, knowledge graphs.

Default style: `sketch` (see `../styles/sketch.md`)

---

## One Diagram = One Conceptual Question

A concept web should answer one question:
- What are the main ideas around this topic and how do they connect?
- How does this concept break into sub-themes?
- What relationships exist between these different ideas?

---

## Canonical Layouts

### Radial (center-out) — default for mind maps
```
           [Sub A]
        ↗
[Core Topic] → [Sub B]
        ↘
           [Sub C]
               ↘
              [Sub C.1]
```
Use for: mind maps, topic exploration, brainstorming.

### Network (freeform positions)
```
[A] ── [B] ── [D]
 |      |
[C] ── [E]
```
Use for: knowledge graphs, relationship maps where no hierarchy exists.

### Cluster Map
```
┌─ Theme 1 ─────┐   ┌─ Theme 2 ─────┐
│ [A]  [B]  [C] │   │ [D]  [E]      │
└───────────────┘   └───────────────┘
         ↕ [cross-theme connection]
```
Use for: organizing multiple distinct themes that share some relationships.

### Hierarchical Breakdown
```
[Root Concept]
    ├── [Category 1]
    │       ├── [Detail]
    │       └── [Detail]
    └── [Category 2]
            └── [Detail]
```
Use for: taxonomies, classifications, structured knowledge.

---

## Required Elements

1. **Central concept** — the root node or main topic
2. **3–6 primary branches** — the main sub-themes or categories
3. **2–4 items per branch** — specific ideas, facts, or sub-concepts
4. **Relationship labels** — at least key connections labeled (not just lines)
5. **Visual distinction** — core node must be visually prominent (larger, different style)

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Core Concept | `ellipse` (large) or bold `text` | Center or top of canvas; visually dominant |
| Primary Branch | `ellipse` (medium) | Main sub-themes |
| Leaf Node | `text` (floating) or small `rectangle` | Specific details |
| Relationship | `line` (undirected) or `arrow` (directed) | Labeled when relationship type matters |
| Theme Cluster | `frame` (light) | Use sparingly for major groupings only |

---

## Hierarchy vs. Network Rule

Choose the right structure:

- **Use hierarchy** if the concept has clear parent-child containment (categories, taxonomies)
- **Use network** if relationships are lateral (associations, influences, cross-references)
- **Use radial** if one concept is clearly central and others orbit it
- **Mix** only if the concept genuinely has both structure and lateral connections

---

## Label Economy

Mind maps and concept webs tend toward label clutter. Apply these rules:

- Each node label = 1–4 words
- Relationship labels on edges = 1–3 words (e.g., "leads to", "part of", "example of")
- If a concept needs explanation, add it as a floating annotation — not inside the node
- Remove nodes that are only there to pad the diagram

---

## Anti-Patterns

- All nodes the same size and shape (no visual hierarchy)
- Arrows without direction or label when the relationship has a specific type
- More than 50 nodes in one diagram (split into multiple diagrams)
- Dense overlapping lines in the center of a radial layout
- Text paragraphs inside nodes
