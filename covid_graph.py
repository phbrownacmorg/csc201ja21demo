# Draw a bar graph of Spartanburg County COVID cases, 1/10/21 - 1/16/21
# Source: https://scdhec.gov/covid19/south-carolina-county-level-data-covid-19, visited 2021-01-19
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    width:int = 400
    height:int = 400
    w:GraphWin = GraphWin("Click to close", width, height)

    # Data:
    dates:List[str] = ['1/10', '1/11', '1/12', '1/13', '1/14', '1/15', '1/16']
    cases:List[int] = [128, 267, 229, 127, 218, 237, 99]

    # Draw axes
    border:int = 25
    origin_x:int = border
    origin_y:int = height - border
    top_y:int = border
    right_x:int = width - border

    origin:Point = Point(origin_x, origin_y)
    x_axis:Line = Line(origin, Point(right_x + border//2, origin_y))
    x_axis.setArrow('last')
    x_axis.draw(w)
    y_axis:Line = Line(origin, Point(origin_x, top_y + border//2))
    y_axis.setArrow('last')
    y_axis.draw(w)

    graph_width:int = width - 2 * border
    graph_height:int = height - 2 * border

    # Y-axis labels
    day_width:int = graph_width // len(dates)
    maxval:int = max(cases)
    for i in range(len(dates)):
        # Y-axis label
        label:Text = Text(Point(origin_x + (i + 0.5)* day_width, origin_y + border/2), dates[i])
        label.draw(w)

        # Bar
        bar = Rectangle(Point(origin_x + i * day_width, origin_y), Point(origin_x + (i+1) * day_width, origin_y - (cases[i]/maxval)*graph_height))
        bar.setFill('cyan')
        bar.draw(w)


    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)