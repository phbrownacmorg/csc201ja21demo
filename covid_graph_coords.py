# Draw a bar graph of Spartanburg County COVID cases, 1/10/21 - 1/16/21
# Source: https://scdhec.gov/covid19/south-carolina-county-level-data-covid-19, visited 2021-01-19
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Data:
    dates:List[str] = ['1/10', '1/11', '1/12', '1/13', '1/14', '1/15', '1/16']
    cases:List[int] = [128, 267, 229, 127, 218, 237, 99]
    maxY:int = max(cases)
    maxX:int = len(dates)

    w:GraphWin = GraphWin("Click to close", 400, 400)
    font_size:int = 10
    border:float = .1
    x_border:float = border * maxX
    y_border:float = border * maxY
    w.setCoords(-x_border, -y_border,
                maxX + x_border, maxY + y_border)

    # Draw axes
    origin:Point = Point(0, 0)
    x_axis:Line = Line(origin, 
                    Point(maxX + x_border/2, 0))
    x_axis.setArrow('last')
    x_axis.draw(w)
    y_axis:Line = Line(origin, 
                    Point(0, maxY + y_border/2))
    y_axis.setArrow('last')
    y_axis.draw(w)

    for i in range(len(dates)):
        # X-axis label
        label:Text = Text(Point(i + 0.5, -y_border/3), dates[i])
        label.setSize(font_size)
        label.draw(w)

        # Bar
        bar = Rectangle(Point(i, 0), 
                         Point(i+1, cases[i]))
        bar.setFill('cyan')
        bar.draw(w)

        # Data labels
        label = Text(Point(i + 0.5, 
                        cases[i] + y_border/4),
                     str(cases[i]))
        label.setSize(font_size)
        label.draw(w)

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)