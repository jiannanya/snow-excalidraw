# Timeline View Diagrams

Use this guide when the goal is to show chronological sequences, project roadmaps, historical timelines, protocol event sequences, or sprint planning.

Default style: `clean` (see `../styles/clean.md`)

---

## Canonical Layouts

### Horizontal Timeline (default for roadmaps)
```
──●─────────●──────────●──────────●──
Q1        Q2          Q3          Q4
[Alpha]  [Beta]    [Launch]   [v2.0]
```
Use for: product roadmaps, project milestones, release schedules.

### Vertical Timeline (for sequences)
```
●── Event A (t=0)
│
●── Event B (t=200ms)
│
●── Event C (t=450ms)
│
●── Event D (t=800ms)
```
Use for: protocol sequences, message order, API call chains, incident timelines.

### Swimlane Timeline (multi-actor)
```
[Actor A] ──●──────●──────────────●──
[Actor B] ──────●──────●──────●──────
[Actor C] ────────────────●──────────
           t0   t1    t2    t3    t4
```
Use for: distributed system message sequences, collaboration flows, multi-stakeholder processes.

### Gantt-Style (duration bars)
```
Task A    [████████]
Task B         [████████████]
Task C              [██████]
          Jan  Feb  Mar  Apr  May
```
Use for: project schedules, dependency planning, sprint overview.

---

## Required Elements

1. **Spine** — the backbone line (`line` element) running the full length of the timeline
2. **Milestones / events** — small dots or markers at key points
3. **Labels** — every milestone has a label (what happened)
4. **Time anchors** — dates, versions, or relative times at regular intervals
5. **At least one "before and after"** — show what changed over time, not just event names

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Timeline spine | `line` | Straight, full-width; horizontal or vertical |
| Milestone dot | `ellipse` (12–16px, filled) | Positioned on the spine |
| Event label | `text` (floating) | Above the spine = past; below = future (horizontal) |
| Duration bar | `rectangle` (long, thin) | No border; use `backgroundColor` for fill |
| Time label | `text` (floating) | Date, quarter, sprint number |
| Phase boundary | `line` (dashed, vertical) | Separates phases or time periods |
| Annotation | `text` (floating, small) | Extra context for a specific event |

---

## Swimlane Rule

For swimlane timelines:
- One `line` spine per actor
- Actor names as left-aligned `text` labels beside their spine
- Use a `frame` only if the number of swimlanes exceeds 4 and grouping helps readability

---

## Sequence Diagram Protocol

For protocol / message sequence diagrams:
- Spines are **vertical** (one per actor)
- Arrows go **horizontal** between spines (labeled with the message name)
- Time flows **downward**
- Include timing annotations (latency, retries, timeouts) as floating text

---

## Anti-Patterns

- Long timeline with no time anchors (the reader cannot locate events in time)
- Events without labels (unlabeled milestones are meaningless)
- Mixing two different timelines on the same spine
- More than 12 milestones on one horizontal spine without grouping by phase
- Swimlane diagrams where actors don't interact (should be separate timelines)
