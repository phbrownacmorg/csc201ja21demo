# Do nothing with graphics, successfully
# Peter Brown <peter.brown@converse.edu>, 2020-01-14

from graphics import *
from typing import List

def makeButton(p1:Point, p2:Point, label:str, w:GraphWin) -> Rectangle:
    """This function takes two Points a string, and a GraphWin. The function makes a button (Rectangle) defined by the two Points, puts a Text object in the middle showing the string, and uses the GraphWin to draw the whole thing.  The Rectangle is returned, so it can be used to check whether mouse clicks are in the button or not."""
    button:Rectangle = Rectangle(p1, p2)
    buttonText:Text = Text(button.getCenter(), label)
    button.draw(w)
    buttonText.draw(w)
    return button

def inButton(click:Point, button:Rectangle) -> bool:
    """Takes a Point and a Rectangle and returns True if and only if the Point is in the Retangle."""
    p1:Point = button.getP1()
    p2:Point = button.getP2()
    minX:float = min(p1.getX(), p2.getX())
    maxX:float = max(p1.getX(), p2.getX())
    minY:float = min(p1.getY(), p2.getY())
    maxY:float = max(p1.getY(), p2.getY())
    return (minX <= click.getX() <= maxX) and (minY <= click.getY() <= maxY)

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Click to close", 350, 350)
    w.setCoords(-1, -1, 1, 1)

    button:Rectangle = makeButton(Point(0, 0), Point(1, 1), 'Quit', w)

    # Listen for a mouse click before closing
    click:Point = w.getMouse()
    while (not inButton(click, button)):
        click = w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)