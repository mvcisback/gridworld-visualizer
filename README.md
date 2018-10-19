# gridworld-visualizer

<object data="assets/example.svg" type="image/svg+xml">
  <img src="assets/example.svg" />
</object>

This is a small library for visualizing gridworlds by generating svgs
styled and animated by css. The api of `gridworld-visualizer` centers
around the `gridworld` function.
```python
gridworld(n=10, actions=None, tile2classes=None, extra_css="") -> SVG
```
which takes in the dimension of the gridworld (currently assumed to
be a square `n x n`), the sequence of actions (currently support moving
in the cardinal directions), and a function
```python
tile2classes(x: int, y: int) -> str
```
which given a grid cell `(x, y)` returns a string for its
type. Currently, the default styling supports, "water", "recharge",
"dry", "lava", and "normal". As these types just correspond to css
classes, one can add additional styling using the `extra_css` option.

## Example
Below we generate the gridworld from at the top of the page, (originally from [Vazquez-Chanlatte, Marcell, et al. "Learning Task Specifications from Demonstrations."](https://arxiv.org/abs/1710.03875)).
```python
import gridworld_visualizer as gv


def tile2classes(x, y):
    if (3 <= x <= 4) and (2 <= y <= 5):
        return "water"
    elif (x in (0, 7)) and (y in (0, 7)):
        return "recharge"
    elif (2 <= x <= 5) and y in (0, 7):
        return "dry"
    elif x in (1, 6) and (y in (4, 5) or y <= 1):
        return "lava"
    elif (x in (0, 7)) and (y in (1, 4, 5)):
        return "lava"

    return "normal"

actions = [gv.E, gv.N, gv.N, gv.N, gv.N, gv.W, gv.W, gv.W]
svg = gv.gridworld(n=8, tile2classes=tile2classes, actions=actions)
svg.saveas("example.svg", pretty=True)
```
