# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Click to close", 400, 400)
    w.setCoords(-1, -1, 1, 1)

    rodent:Circle = Circle(Point(0, 0), 0.05)
    rodent.setFill('gray')
    rodent.draw(w)

    numclicks:int = 5
    for i in range(numclicks):
        click:Point = w.getMouse()
        rodentPt:Point = rodent.getCenter()
        dx:float = click.getX() - rodentPt.getX()
        dy:float = click.getY() - rodentPt.getY()
        rodent.move(dx, dy)

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)