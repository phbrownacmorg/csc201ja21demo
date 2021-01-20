# Do nothing with graphics, successfully
# Peter Brown, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Convert temperatures", 400, 400)
    w.setCoords(-1, -1, 1, 1)

    c_label:Text = Text(Point(-0.75, 0), '\u00b0C: ')
    c_label.draw(w)
    c_entry:Entry = Entry(Point(-0.5, 0), 5)
    c_entry.draw(w)

    f_label:Text = Text(Point(0.5, 0), '\u00b0F:      ')
    f_label.draw(w)

    instructions:Text = Text(Point(0, 0.8), "Click to convert")
    instructions.draw(w)

    # Wait for a click
    w.getMouse()
    degC:float = float(c_entry.getText())
    degF:float = (9/5) * degC + 32
    f_label.setText('\u00b0F: ' + str(round(degF, 2)))

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)