# Calculate the future value of an investment
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List, Tuple
from graphics import *

def readParams() -> Tuple[float, float, int]:
    # Read from the keyboard: amount, interest rate, periods
    # read the amount (principal)
    P:float = float(input('Please enter the amount to invest: $'))
    rate:float = float(input('Please enter the interest rate per period, with no %: '))
    periods:int = int(input('Please enter the number of periods: '))

    # Clamp the input values to make them at least slightly sensible
    P = max(P, 0.01)          # Force P >= $0.01
    rate = max(rate, 0)       # Force rate >= 0
    periods = max(periods, 1) # Force periods > 0

    # Adjust the rate from a percentage to a raw number
    rate = rate/100

    return P, rate, periods

def calcFutureval(P:float, rate:float, periods:int) -> List[float]:
    # Accumulator variable
    values:List[float] = [P]
    for i in range(periods):
        # Calculate the interest
        interest = P * rate
        # Add the interest back into the principal (accumulate)
        P = P + interest
        # Append to the List
        values.append(P)
    return values

def printTable(P:float, rate:float, amounts:List[float]) -> None:
    # Print out the initial parameters
    print('Investing $' + str(amounts[0]), 'at', str(rate*100) + "% for", len(amounts)-1, 'periods.')
    # Calculate and print out the investment table
    # Print a header row
    print('\n{0:7}   {1:^10}     {2:^11}'.format('Period','Interest',   'Amount'))
    print('-' * 36)
    # Print the starting amount
    print('Initial{0:18}${1:>10.2f}'.format(' ', amounts[0]))
    # Print out the table, row by row
    for i in range(1, len(amounts)):
        # Calculate the interest
        interest:float = amounts[i] - amounts[i-1]
        # Print the table row
        print('{0:>5}     ${1:>9.2f}     ${2:>10.2f}'.format(i, interest, amounts[i]))

def makeAxis(endpt:Point) -> Line:
    """Make and return an axis from the origin to endpt."""
    axis:Line = Line(Point(0, 0), endpt)
    axis.setArrow('last')
    return axis

def drawGraph(amounts:List[float]) -> None:
    """Draw a graph of the given amounts."""
    w:GraphWin = GraphWin("Future values", 350, 350)
    maxX:int = len(amounts)
    maxY:float = max(amounts)
    border:float = 0.1
    x_border:float = border * maxX
    y_border:float = border * maxY
    w.setCoords(-x_border, -y_border, maxX + x_border,
            maxY + y_border)

    # Axes
    makeAxis(Point(maxX + (x_border/2), 0)).draw(w)
    makeAxis(Point(0, maxY + (y_border/2))).draw(w)

    for i in range(len(amounts)):
        bar:Rectangle = Rectangle(Point(i, amounts[i]), 
                                Point(i+1, 0))
        bar.setFill('green')
        bar.draw(w)

    # Listen for a mouse click before closing
    w.getMouse()
    w.close()

def main(args:List[str]) -> int:
    P, rate, periods = readParams() # type: Tuple(float, float, int)
    amounts:List[float] = calcFutureval(P, rate, periods)
    printTable(P, rate, amounts)
    drawGraph(amounts)
    return 0

if __name__ == "__main__":
    import sys   
    main(sys.argv)