# Anti-Patterns Reference

A catalog of common diagram mistakes and how to fix them.

---

## Anti-Pattern 1: The Uniform Box Grid

**What it looks like:**
```
[Box 1] [Box 2] [Box 3]
[Box 4] [Box 5] [Box 6]
```
Every element is a rectangle of identical size, uniformly spaced, with one-word labels.

**Why it's wrong:** No visual hierarchy. The reader cannot tell which elements matter more. The diagram looks like a spreadsheet, not a communication tool.

**Fix:** 
- Make the central or most important element larger
- Use different shapes for different roles (ellipse for actors, diamond for decisions)
- Group related elements into frames
- Use whitespace to create visual clusters

---

## Anti-Pattern 2: The Arrow Spaghetti

**What it looks like:**
Multiple arrows crossing each other, cutting through boxes, routing in unpredictable directions.

**Why it's wrong:** The reader cannot trace individual relationships. The diagram looks chaotic.

**Fix:**
- Route arrows through whitespace first
- Add intermediate points to bend arrows around boxes
- If routing is impossible, split the diagram into two
- Use a flow spine with local arrows instead of one giant connector

---

## Anti-Pattern 3: The Text Dump

**What it looks like:**
```
[This component handles user authentication by validating the JWT token,
 checking the expiry time, and querying the user database to retrieve
 user permissions...]
```
Paragraph text inside a shape.

**Why it's wrong:** Diagrams are not documents. Paragraphs inside shapes are unreadable at diagram scale and defeat the purpose of visual communication.

**Fix:**
- Max 5 words per shape label
- Move long explanations to floating annotations outside the shape
- If you need paragraphs, the right format is a document, not a diagram

---

## Anti-Pattern 4: Missing Error / Failure Paths

**What it looks like:**
```
[Input] → [Process] → [Output]
```
Only the happy path is shown.

**Why it's wrong:** Real systems fail. A diagram that doesn't show failure modes is incomplete and misleading.

**Fix:**
- Add a `diamond` for every significant decision
- Show at least one error or fallback path
- Use dashed arrows for failure/fallback routes
- Add a "dead letter" or "error state" node

---

## Anti-Pattern 5: Unlabeled Arrows

**What it looks like:**
```
[Service A] ──────→ [Service B]
```
Arrow with no label, no protocol, no event name.

**Why it's wrong:** The relationship between A and B is unknown. The diagram says "they connect" but not "how" or "what."

**Fix:**
- Label every arrow with the protocol (`HTTP POST`, `gRPC`, `Kafka event`)
- Or label with the data type (`JSON payload`, `user record`)
- Or label with the trigger (`on login`, `every 5 minutes`)

---

## Anti-Pattern 6: The Everything Diagram

**What it looks like:**
A single diagram with 30+ elements covering the entire system architecture, all user journeys, all data flows, all team responsibilities.

**Why it's wrong:** No one can read it. The diagram tries to answer everything and answers nothing clearly.

**Fix:**
- Pick one question per diagram
- Create multiple focused diagrams
- Use frames to suggest "detail view" for sub-systems

---

## Anti-Pattern 7: Style Inconsistency

**What it looks like:**
Some elements use roughness=0, others roughness=1. Some text is Virgil, other text is Helvetica. Some strokes are blue, others are black.

**Why it's wrong:** Looks unfinished. Visual inconsistency distracts from the content.

**Fix:**
- Choose one style (sketch/blueprint/clean/dark) and apply it to every element
- Set roughness, fontFamily, strokeColor consistently
- Review style against `../styles/<chosen-style>.md` before delivery

---

## Anti-Pattern 8: Decorative Color

**What it looks like:**
Each service or component has a different background color — red, blue, green, purple, orange — for "visual variety."

**Why it's wrong:** Colors imply semantic meaning. Random colors confuse the reader who expects color to mean something.

**Fix:**
- Use color only for semantic reasons (error = red, success = green, accent = blue)
- Default to monochrome for sketch and blueprint styles
- Apply one accent color maximum per diagram

---

## Anti-Pattern 9: The Phantom Diagram

**What it looks like:**
The diagram URL is shared, but the `.excalidraw` file has an empty elements array, or the file was never written.

**Why it's wrong:** The hosted URL encodes the file content. An empty file produces a blank diagram.

**Fix:**
- Always write the `.excalidraw` file with a non-empty elements array before generating any URL
- Run the validator (`validate.py`) to confirm the file is valid before opening
- Never call `open.py` before `validate.py` exits 0

---

## Anti-Pattern 10: Missing Binding References

**What it looks like:**
A shape has `boundElements: [{"id": "txt-abc", "type": "text"}]` but `txt-abc` doesn't exist in the elements array. Or a text element has `containerId: "rect-xyz"` but `rect-xyz` is gone.

**Why it's wrong:** Excalidraw renders this incorrectly; the text may float free or appear detached.

**Fix:**
- When deleting an element, remove all references to it from other elements' `boundElements`
- When renaming an ID, update all references
- Run `validate.py` — it catches all broken reference pairs
