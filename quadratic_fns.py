# Solve a quadratic equation
# Peter Brown <peter.brown@converse.edu>, 2021-02-01

from typing import List, Optional, Tuple
import math # So Python knows that the name "math" means to go look in the math library

# Input
def readCoefficients() -> Tuple[float, float, float]:
    """Read the coefficients of a quadratic equation from the keyboard.  The coefficients are returned as a tuple."""
    print('This program finds roots for a quadratic system a*x**2 + b*x + c = 0.')
    a = float(input("Please enter a value for a: "))
    b = float(input("Please enter a value for b: "))
    c = float(input("Please enter a value for c: "))
    return a, b, c

# Process
def findRoots(a:float, b:float, c:float) -> Tuple[float, float]:
    """Given the coefficients a, b, and c of a quadratic equation, find and return its roots.  If the equation has no real roots, the tuple (None, None) is returned."""
    det:float = b**2 - 4*a*c
    root1:float = (-b + math.sqrt(det)) / (2*a)
    root2:float = (-b - math.sqrt(det)) / (2*a)
    return root1, root2

def main(args:List[str]) -> int:
    # Get the quadratic equation from the keyboard
    try:
        a, b, c = readCoefficients()
    except ValueError: # They weren't all numbers
        print('a, b, and c must all be numbers.')
    else:
        print('The system is', a, "* x**2 +", b, '* x +', c, '= 0')
        # Find the roots (if they exist)
        try:
            root1, root2 = findRoots(a, b, c)
        except ValueError: # What kind of error?
            print('The system has no real roots.')
        else:
            print('The roots are', root1, 'and', root2)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)
