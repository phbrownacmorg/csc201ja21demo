# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import cast, List, Tuple
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
    cx:float = center.getX()
    cy:float = center.getY()
    ear:Polygon = Polygon(
        Point(cx + sign * r * math.cos(math.radians(40)),
              cy + r * math.sin(math.radians(40))),
        Point(cx + sign * 1.9 * r * math.cos(math.radians(60)),
                cy + 1.9 * r * math.sin(math.radians(60))),
        Point(cx + sign * r * math.cos(math.radians(80)),
              cy + r * math.sin(math.radians(80))))
    ear.setFill('orange')
    ear.setOutline('orange')
    return ear

def makeNose(center:Point, r:float) -> Polygon:
    cx:float = center.getX()
    cy:float = center.getY()
    nose:Polygon = Polygon(Point(cx, cy - r * 0.2),
                           Point(cx - r*0.15, cy), 
                           Point(cx + r*0.15, cy))
    nose.setFill('black')
    nose.setOutline('black')
    return nose

def makeMouth(center:Point, r:float) -> Tuple[Line, Line]:
    cx:float = center.getX()
    cy:float = center.getY()
    middlePt:Point = Point(cx, cy - r * 0.4)
    vertical:Line = Line(Point(cx, cy - r * 0.2), middlePt)
    leftSide:Line = Line(middlePt, 
                        Point(cx + r * 0.4, cy - r * 0.5))
    rightSide:Line = Line(middlePt, 
                        Point(cx - r * 0.4, cy - r * 0.5))
    return vertical, leftSide, rightSide

def makeWhiskers(center:Point, r:float) -> List[Line]:
    cx:float = center.getX()
    cy:float = center.getY()
    angles:Tuple[float, ...] = (10, 0, -10)
    whiskers:List[Line] = []
    for sign in [-1, 1]: # type: int
        for angle in angles: # type: float
            whiskers.append(Line(Point(cx + sign*r*0.8*math.cos(math.radians(angle)), 
                                        cy + r*0.8*math.sin(math.radians(angle))),
                                Point(cx + sign*r*1.8*math.cos(math.radians(angle)), 
                                        cy + r*1.8*math.sin(math.radians(angle)))))
    return whiskers

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
    partsList.append(makeEye(Point(pt.getX() - r*0.5,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() - r * 0.2,
                                pt.getY() + r * 0.1), 'black'))
    partsList.append(makeEye(Point(pt.getX() + r*0.5,
                                pt.getY() + r * 0.8),
                            Point(pt.getX() + r * 0.2,
                                pt.getY() + r * 0.1), 'black'))
    partsList.append(makeNose(pt, r))
    partsList.extend(makeMouth(pt, r))
    partsList.extend(makeWhiskers(pt, r))
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
    partsList.append(makeNose(pt, r))
    partsList.extend(makeMouth(pt, r))
    partsList.extend(makeWhiskers(pt, r))

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