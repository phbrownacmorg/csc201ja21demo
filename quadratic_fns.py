# Solve a quadratic equation
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List, Optional, Tuple
import math # So Python knows that the name "math" means to go look in the math library

# Input
def readCoefficients() -> Tuple[float, float, float]:
    """Read the coefficients of a quadratic equation from the keyboard.  The coefficients are returned as a tuple."""
    print('This program finds roots for a quadratic system a*x**2 + b*x + c = 0.')
    a:float = float(input("Please enter a value for a: "))
    b:float = float(input("Please enter a value for b: "))
    c:float = float(input("Please enter a value for c: "))
    return a, b, c

# Process
def findRoots(a:float, b:float, c:float) -> Tuple[Optional[float], Optional[float]]:
    """Given the coefficients a, b, and c of a quadratic equation, find and return its roots.  If the equation has no real roots, the tuple (None, None) is returned."""
    det:float = b**2 - 4*a*c
    root1:Optional[float] = None
    root2:Optional[float] = None
    if det >= 0:
        root1 = (-b + math.sqrt(det)) / (2*a)
        root2 = (-b - math.sqrt(det)) / (2*a)
    return root1, root2

def main(args:List[str]) -> int:
    # Get the quadratic equation from the keyboard
    a, b, c = readCoefficients()
    print('The system is', a, "* x**2 +", b, '* x +', c, '= 0')
    # Find the roots (if they exist)
    root1, root2 = findRoots(a, b, c)
    # Print the roots
    if root1 is None: # in which case root2 is None also
        print('The system has no real roots.')
    else:
        print('The roots are', root1, 'and', root2)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)
