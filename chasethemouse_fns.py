# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import cast, List
import math

# Define an animal as a List[GraphicsObject].  Item 0 on the list is always a Circle.

def animalCenter(animal:List[GraphicsObject]) -> Point:
    return cast(Circle, animal[0]).getCenter()

def moveAnimal(animal:List[GraphicsObject], 
                dx: float, dy: float) -> None:
    for part in animal:
        part.move(dx, dy)

def drawAnimal(animal:List[GraphicsObject], w:GraphWin) -> None:
    for part in animal:
        part.draw(w)

def makeEye(p1:Point, p2:Point, color:str) -> Oval:
    eye:Oval = Oval(p1, p2)
    eye.setFill(color)
    return eye

def makeMouseEar(center:Point, r:float, sign:float) -> Circle:
    ear_center = Point(center.getX() + sign * 0.6*r,
                        center.getY() + 1.2*r)
    ear:Circle = Circle(ear_center, r * .55)
    ear.setFill('gray')
    ear.setOutline('gray')
    return ear

def makeCatEar(center:Point, r:float, sign:float) -> Polygon:
    ear:Polygon = Polygon(
        Point(center.getX()+sign*r*math.cos(math.radians(40)),          center.getY() + r * math.sin(math.radians(40))),
        Point(center.getX()+sign*1.9*r*math.cos(math.radians(60)),
                center.getY()+1.9*r*math.sin(math.radians(60))),
        Point(center.getX()+sign*r*math.cos(math.radians(80)),          center.getY() + r * math.sin(math.radians(80))))
    ear.setFill('orange')
    ear.setOutline('orange')
    return ear

def makeMouse(pt:Point, w:GraphWin) -> List[GraphicsObject]:
    partsList:List[GraphicsObject] = []
    r:float = 0.05
    head:Circle = Circle(pt, r)
    head.setFill('gray')
    partsList.append(head)

    # Ears
    partsList.append(makeMouseEar(pt, r, -1))
    partsList.append(makeMouseEar(pt, r, 1))
    # Eyes
    partsList.append(makeEye(Point(pt.getX() - r*0.4,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() - r * 0.2,
                                pt.getY()), 'black'))
    partsList.append(makeEye(Point(pt.getX() + r*0.4,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() + r * 0.2,
                                pt.getY()), 'black'))


    drawAnimal(partsList, w)
    return partsList

def makeCat(pt:Point, w:GraphWin) -> List[GraphicsObject]:
    partsList:List[GraphicsObject] = []
    r:float = 0.2
    head:Circle = Circle(pt, r)
    head.setFill('orange')
    partsList.append(head)
    # Ears
    partsList.append(makeCatEar(pt, r, -1))
    partsList.append(makeCatEar(pt, r, 1))
    # Eyes
    partsList.append(makeEye(Point(pt.getX() - r*0.6,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() - r * 0.1,
                                pt.getY()), 'green'))
    partsList.append(makeEye(Point(pt.getX() + r*0.6,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() + r * 0.1,
                                pt.getY()), 'green'))
    drawAnimal(partsList, w)
    return partsList

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Click to close", 350, 350)
    w.setCoords(-1, -1, 1, 1)

    rodent:List[GraphicsObject] = makeMouse(Point(0,0), w)
    cat:List[GraphicsObject] = makeCat(Point(-1,1), w)

    numclicks:int = 5
    for i in range(numclicks):
        click:Point = w.getMouse()
        rodentPt:Point = animalCenter(rodent)
        dx:float = click.getX() - rodentPt.getX()
        dy:float = click.getY() - rodentPt.getY()
        moveAnimal(rodent, dx, dy)

        catPt:Point = animalCenter(cat)
        dx = rodentPt.getX() - catPt.getX()
        dy = rodentPt.getY() - catPt.getY()
        moveAnimal(cat, dx, dy)

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)