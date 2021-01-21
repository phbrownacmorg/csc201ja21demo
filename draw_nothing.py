# Do nothing with graphics, successfully
# Peter Brown <peter.brown@converse.edu>, 2020-01-14

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    w:GraphWin = GraphWin("Click to close", 400, 400)

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)