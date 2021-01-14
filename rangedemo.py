# Demonstrate the range() function
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def main(args:List[str]) -> int:
    # One-argument range(stopval) function
    # from 0 up to (but not including) stopval
    print('One-argument range(stop):')
    print('range(10) =', list(range(10)))
    print('range(5) =', list(range(5)))

    # Two-argument range(start, stop) function
    # From start up to (but not including) stop
    print('\nTwo-argument range(start, stop)')
    print('range(2, 10) =', list(range(2, 10)))
    print('range(-5, 6) =', list(range(-5, 6)))

    # Three-argument range(start, stop, step) function
    # From start up to (but not including) stop by step
    print('\nThree-argument range(start, stop, step)')
    print('range(2, 10, 2) =', list(range(2, 10, 2)))
    print('range(-5, 6, 5) =', list(range(-5, 6, 5)))
    print('range(10, 0, -1) =', list(range(10, 0, -1)))

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)

    