# Do nothing with graphics, successfully
# Peter Brown <peter.brown@converse.edu>, 2020-01-14

from graphics import *
import math
from typing import List

def distance(p1:Point, p2:Point) -> float:
    dx:float = p1.getX() - p2.getX()
    dy:float = p1.getY() - p2.getY()
    return math.sqrt(dx**2 + dy**2)

def drawTriangle(win:GraphWin, instr:Text) -> None:
    instructions:List[str] = ['Click to set a vertex',
        'Click again to set another vertex',
        'Click again to draw']
    # Accumulator variable
    vertices:List[Point] = []
    # Loop
    for i in range(3):
        instr.setText(instructions[i])
        p:Point = win.getMouse()
        p.draw(win)
        vertices.append(p) # Update the accumulator variable

    # I have 3 clicks.  Now draw the triangle.
    poly:Polygon = Polygon(vertices)
    poly.draw(win)

    # Accumulator pattern, again
    
    # Accumulator pattern #2
    # Accumulator variable #2
    perimeter:float = 0 # Adding to it
    maxX:float = vertices[0].getX()
    minX:float = vertices[0].getX()
    maxY:float = vertices[0].getY()
    minY:float = vertices[0].getY()

    # Loop for accumulator #2
    for i in range(1, 3):
        # Update accumulator variable #2
        perimeter += distance(vertices[i], vertices[i-1])
        maxX = max(maxX, vertices[i].getX())
        minX = min(minX, vertices[i].getX())
        maxY = max(maxY, vertices[i].getY())
        minY = min(minY, vertices[i].getY())
    # Add the side that wasn't caught by the loop
    perimeter += distance(vertices[-1], vertices[0])

    area:float = (maxX - minX) * (maxY - minY) * 0.5

    info:Text = Text(Point(0, -0.85), 'Area = {0:.3f}\nPerimeter = {1:.3f}'.format(area, perimeter))
    info.draw(win)

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Draw triangle", 350, 350)
    w.setCoords(-1, -1, 1, 1)
    instr:Text = Text(Point(0, 0.9), "")
    instr.draw(w)

    drawTriangle(w, instr)
    instr.setText('Click again to exit')

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)