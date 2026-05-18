# Layout Grid System

Use this guide to position elements on the canvas without guessing coordinates.

---

## Canvas Coordinate System

- Origin: top-left `(0, 0)`
- X increases rightward
- Y increases downward
- Default canvas size: **1400 × 900 px**

---

## Standard Grid

The canvas is divided into a 6-column × 7-row grid. Each cell is 220 × 120 px with 20 px gutters.

```
Col →    C1      C2      C3      C4      C5      C6
Row ↓
R1       80,80   300,80  520,80  740,80  960,80  1180,80
R2       80,200  300,200 520,200 740,200 960,200 1180,200
R3       80,320  300,320 520,320 740,320 960,320 1180,320
R4       80,440  300,440 520,440 740,440 960,440 1180,440
R5       80,560  300,560 520,560 740,560 960,560 1180,560
R6       80,680  300,680 520,680 740,680 960,680 1180,680
R7       80,800  300,800 520,800 740,800 960,800 1180,800
```

**One top-level element per cell.** Bound text elements share their container's cell.

---

## Element Sizing Defaults

| Element Type | Width | Height | Notes |
|---|---|---|---|
| Rectangle (standard) | 200 | 80 | Services, steps, screens |
| Rectangle (tall, content) | 200 | 160 | Panels with multiple lines |
| Rectangle (wide, header) | 420 | 60 | Section headers, full-width labels |
| Ellipse (standard) | 160 | 80 | Actors, concepts |
| Ellipse (circle) | 80 | 80 | Markers, nodes |
| Diamond | 160 | 100 | Decision nodes |
| Frame (small zone) | 420 | 300 | Groups 2-4 elements |
| Frame (large zone) | 660 | 400 | Groups 5-8 elements |

---

## Arrow Coordinate Formula

For horizontal arrows (left-to-right flow):
```
x = source.x + source.width + 5
y = source.y + source.height / 2
width = target.x - source.x - source.width - 10
height = 0
points = [[0, 0], [width, 0]]
```

For vertical arrows (top-to-bottom flow):
```
x = source.x + source.width / 2
y = source.y + source.height + 5
width = 0
height = target.y - source.y - source.height - 10
points = [[0, 0], [0, height]]
```

For bent arrows (around a box):
```
points = [[0, 0], [0, midY], [targetDeltaX, midY], [targetDeltaX, targetDeltaY]]
```

---

## Title Placement

Always place the diagram title at `(80, 20)` with `width: 800, height: 30`.

```
(80, 20)  ← Title text element always here
(80, 80)  ← First content row starts here
```

---

## Common Layout Templates

### Linear Flow (left-to-right, 4 nodes)
```
R2,C1 → R2,C2 → R2,C3 → R2,C4
```
Element x positions: 80, 300, 520, 740

### Top-to-Bottom Flow (3 stages)
```
R1,C3
  ↓
R2,C3
  ↓
R3,C3
```
Element y positions: 80, 200, 320

### Radial (center-out, 5 nodes)
```
Center: R4,C3 (520, 440)
North: R2,C3 (520, 200)
East: R4,C5 (960, 440)
South: R6,C3 (520, 680)
West: R4,C1 (80, 440)
```

### Two-Column Comparison
```
Left panel:  x=80,  y=120, width=580, height=600
Right panel: x=740, y=120, width=580, height=600
Divider:     x=670, y=120, height=600
```

### Swimlane (3 actors, horizontal)
```
Actor 1 spine: y=180
Actor 2 spine: y=340
Actor 3 spine: y=500
Actor labels:  x=40, vertically centered on each spine
Events start:  x=160, spaced 200px apart
```

---

## Overflow Rule

If you need more than 42 elements (6×7 grid), choose one of:
1. Reduce element count by removing non-essential nodes
2. Use a wider canvas (extend to 1800px) and add a 7th column at x=1400
3. Use frames to group related sub-diagrams and refer to them as "detail view"
