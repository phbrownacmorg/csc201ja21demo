# Draw a line specified by two mouse clicks
# Peter Brown <peter.brown@converse.edu>, 2020-01-21

from graphics import *
from typing import List
import math

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Draw a line", 400, 400)
    w.setCoords(-1, -1, 1, 1)

    fontsize = 8

    instructions:Text = Text(Point(0, 0.9), 'Click to set one end of a line')
    instructions.setSize(fontsize)
    instructions.draw(w)

    p1:Point = w.getMouse()
    p1.draw(w)
    instructions.setText('Click again to set the other end')

    p2:Point = w.getMouse()
    p2.draw(w)
    line:Line = Line(p1, p2)
    line.draw(w)

    x1:float = p1.getX()
    y1:float = p1.getY()
    x2:float = p2.getX()
    y2:float = p2.getY()
    d:float = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    output:Text = Text(Point(0, -0.8), 'The distance from ({0:.3f}, {1:.3f}) to ({2:.3f}, {3:.3f})\nis {4:.3f}'.format(x1, y1, x2, y2, d))
    output.setSize(fontsize)
    output.draw(w)

    # Listen for a mouse click before closing
    instructions.setText('Click once more to exit')
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)