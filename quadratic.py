# Solve a quadratic equation
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List
import math # So Python knows that the name "math" means to go look in the math library

def main(args:List[str]) -> int:
    # Get the quadratic equation from the keyboard
    print('This program finds roots for a quadratic system a*x**2 + b*x + c = 0.')
    a:float = float(input("Please enter a value for a: "))
    b:float = float(input("Please enter a value for b: "))
    c:float = float(input("Please enter a value for c: "))
    print('The system is', a, "* x**2 +", b, '* x +', c, '= 0')
    # Find the roots (if they exist)
    det:float = b**2 - 4*a*c
    root1:float = (-b + math.sqrt(det)) / (2*a)
    root2:float = (-b - math.sqrt(det)) / (2*a)
    # Print the roots
    print('The roots are', root1, 'and', root2)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)
