# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Click to close", 400, 400)

    center:Point = Point(200, 200)
    center.setOutline('green')
    center.draw(w)

    diag:Point = Point(300, 300)
    diag.setOutline('purple')
    diag.draw(w)

    L1:Line = Line(center, diag)
    L1.setOutline('red')
    L1.setArrow('both')
    L1.draw(w)

    circ:Circle = Circle(center, 55)
    circ.setOutline('orange')
    circ.setFill('blue')
    circ.draw(w)

    updiag:Point = Point(300, 100)
    rect:Rectangle = Rectangle(center, updiag)
    rect.setFill('cyan')
    rect.draw(w)

    ova:Oval = Oval(center, updiag)
    ova.setFill('magenta')
    ova.draw(w)

    poly:Polygon = Polygon(center, updiag, Point(150, 175))
    poly.setFill('yellow')
    poly.draw(w)

    t:Text = Text(Point(200, 59), 'What a jumble!')
    t.draw(w)

    # Aliasing! More than one name for a single object
    diag.move(-200, -200) # To (100, 100)
    # If you were thinking of L1 as going from center to diag, this would be confusing

    L1c:Point = L1.getCenter()
    print('Center of L1: (', L1c.getX(), ',', L1c.getY(), ')', sep='')

    L2:Line = L1 # Names L2 and L1 refer to the same object
    # Change the object using the L2 name
    L2.move(-150, 0)

    # Why doesn't this come out the same as before?
    # I didn't touch L1!
    L1c:Point = L1.getCenter()
    print('Center of L1: (', L1c.getX(), ',', L1c.getY(), ')', sep='')

    L3:Line = L1.clone() # No aliasing; different objects
    # Change the object using the L3 name
    L3.draw(w)
    L3.move(150, 0)

    # Does come out same as before
    L1c:Point = L1.getCenter()
    print('Center of L1: (', L1c.getX(), ',', L1c.getY(), ')', sep='')
    

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))