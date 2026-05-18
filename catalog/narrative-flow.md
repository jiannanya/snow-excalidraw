# Narrative Flow Diagrams

Use this guide when the goal is to explain a concept, tell a story through a diagram, teach how something works, or create an explainer visual.

Default style: `sketch` (see `../styles/sketch.md`)

---

## One Diagram = One Explanatory Answer

A narrative flow diagram answers one question:
- How does this work, explained visually?
- What is the core story of this concept?
- How do I make this idea stick in someone's memory?

---

## Canonical Layouts

### Linear Story (left-to-right or top-to-bottom)
```
[Setup] → [Conflict / Problem] → [Resolution] → [Outcome]
```
Use for: before/after explanations, problem-solution narratives, process walkthroughs.

### Hero + Context (annotated object)
```
     Note A
       ↑
Note B ← [Central Visual] → Note C
       ↓
     Note D
```
Use for: explaining one key concept with surrounding context, product explainers.

### Cause → Effect Chain
```
[Root Cause] → [Effect 1] → [Effect 2] → [Final Outcome]
                    ↓
              [Side Effect]
```
Use for: root cause analysis, consequence diagrams, cascading effect explanations.

### Comparative Story
```
[Wrong Way]                    [Right Way]
[Step 1: Problem]    vs.       [Step 1: Good Start]
[Step 2: Mistake]              [Step 2: Right Move]
[Step 3: Failure]              [Step 3: Success]
```
Use for: teaching by contrast, best practice illustrations, misconception correction.

---

## Required Elements

1. **One memorable anchor** — the visual element that makes the concept stick (a sketch, a metaphor-shape, an annotated diagram)
2. **Clear problem or tension** — what is being explained, and why it matters
3. **Resolution or answer** — the takeaway or "aha moment"
4. **Concrete example** — one real, grounded example (not abstract labels)

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Memorable anchor | `ellipse` (large) or unique sketch shape | Central visual hook |
| Concept node | `rectangle` or `ellipse` | Supporting ideas |
| Step in sequence | `rectangle` with number label | Sequential steps |
| Annotation | `text` (floating) | Contextual notes; keep brief |
| Connection | `arrow` with label | Labeled with relationship type |
| Example artifact | `rectangle` with monospace text | Real example data, code snippet, or value |
| Metaphor hint | `text` (italic, floating) | E.g., "like a lock and key" |
| Highlight / Callout | `ellipse` or `rectangle` with `strokeWidth: 3` | Draw attention to the key insight |

---

## Teaching Simplicity Rules

1. **Start with the problem, not the solution** — the reader must feel the need before the answer
2. **One concept per shape** — do not cram a paragraph into a box
3. **Use a metaphor sparingly** — one metaphor per diagram; don't mix metaphors
4. **Show, don't tell** — if you can show data, a comparison, or a sketch instead of writing "it works like this", do it
5. **End with the takeaway** — the last element the eye lands on should be the conclusion

---

## Audience Calibration

| Audience | Guidance |
|----------|----------|
| Expert | Use precise technical terms; fewer annotations; trust the reader |
| General | Use plain-language labels; include at least one concrete example |
| Child / beginner | Use metaphors; limit to 5–7 elements; large labels; one concept only |

Default to **general** audience unless the user specifies otherwise.

---

## Anti-Patterns

- Starting with the solution (no setup = no context = no retention)
- All-text diagram with no visual structure
- Abstract shapes with no concrete examples
- Too many concepts (more than 8 nodes) without a clear narrative thread
- No takeaway — the diagram ends without a conclusion
