# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Set a color", 400, 400)
    w.setCoords(-1, -1, 1, 1)
    fontSize:int = 8

    c_label:Text = Text(Point(0, 0.8), '')
    c_label.setText('Color (named): ')
    #c_label.setText('Color (R, G, B): ')
    c_label.setSize(fontSize)
    c_label.draw(w)
    c_entry:Entry = Entry(Point(0, 0.65), 22)
    c_entry.setSize(fontSize)
    c_entry.draw(w)

    box:Rectangle = Rectangle(Point(-0.8, -0.8), Point(0.8, 0.2))
    box.setFill('white')
    box.draw(w)

    instructions:Text = Text(Point(0, 0.4), "Click to change the color of the box")
    instructions.setSize(fontSize)
    instructions.draw(w)

    #print(color_rgb(0,0,255))
    #print(color_rgb('green'))

    for i in range(5):
        # Wait for a click
        w.getMouse()
        # Change the color (named)
        box.setFill(c_entry.getText())
        # Change the color (RGB)
        # rgbStr:str = c_entry.getText()
        # rgbList:List[str] = rgbStr.split(',')
        # rgbNums:List[int] = list(map(int, rgbList))
        # box.setFill(color_rgb(rgbNums[0], rgbNums[1], rgbNums[2]))

    instructions.setText('Click once more to exit')

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)