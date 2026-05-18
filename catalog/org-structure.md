# Org Structure Diagrams

Use this guide when the goal is to show team hierarchies, reporting lines, role maps, or organizational relationships.

Default style: `clean` (see `../styles/clean.md`)

---

## Canonical Layouts

### Top-Down Hierarchy (default)
```
          [CEO]
         /     \
    [CTO]       [CPO]
   /    \          \
[Eng A] [Eng B]  [PM Team]
```
Use for: reporting structures, org charts, management hierarchies.

### Flat Team Map (horizontal)
```
[Team Lead]
    |
[Eng 1] [Eng 2] [Designer] [QA]
```
Use for: small teams, squad structures, cross-functional pods.

### Matrix Structure
```
        [Func A] [Func B] [Func C]
[PM 1]     ●        ●
[PM 2]               ●        ●
[PM 3]     ●                  ●
```
Use for: matrix organizations, program/product allocations.

---

## Required Elements

1. **Root node** — the top of the hierarchy (or the team/group being described)
2. **Direct reports** — one level of children per parent node
3. **Role labels** — job title or function, not just names
4. **Name + role** — include both when relevant; role is primary
5. **Span** — show at most 3 levels of hierarchy in one diagram; deeper = a separate diagram

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Senior leader | `rectangle` (wider, bold label) | Top of hierarchy |
| Manager / Lead | `rectangle` (standard) | Mid-level |
| Individual contributor | `rectangle` (smaller) | Leaf nodes |
| External / Contractor | `rectangle` + `strokeStyle: "dashed"` | Not on the core team |
| Open position | `rectangle` + label "Open Role" | Vacancies |
| Line of reporting | `line` (not arrow) | Undirected connection for hierarchy |
| Dotted-line report | `line` + `strokeStyle: "dashed"` | Indirect or advisory relationship |
| Team / Department | `frame` | Grouping container for team members |

---

## Label Format

Use a consistent two-line label format inside each node:

```
Name / Initials
Role Title
```

Or, for unnamed role maps:
```
Role Title
```

Keep labels to max 2 lines. Do not include email, location, or other metadata inside the node. Add it as a floating annotation if needed.

---

## Depth Rule

Show a maximum of **3 levels** in a single diagram. For deeper organizations:
- Show the top 2–3 levels on the main diagram
- Create a separate diagram for each major sub-tree
- Use a `frame` with a label like "See: Engineering Org" to indicate expansion

---

## Anti-Patterns

- Mixing reporting hierarchy with project assignments on the same diagram
- Drawing the entire company hierarchy in one canvas
- Using arrows instead of lines for organizational reporting (arrows imply directed data flow)
- No visual distinction between levels (all boxes same size)
- Including personal details (email, phone, photo) inside nodes
