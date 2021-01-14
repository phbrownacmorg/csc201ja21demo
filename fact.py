# Find a factorial using the accumulator pattern
# Peter Brown <peter.brown@converse.edu>, 2021-01-13

from typing import List

def main(args:List[str]) -> int:
    """Find a factorial using the accumulator pattern."""
    # Get the number for the factorial.
    n:int = int(input('Please enter a positive integer: '))
    print(str(n) + '! = ', end='')

    # Accumulator pattern: initialize the accumulator variable
    product:int = 1 # (identity element for multiplication)

    for i in range(1,n+1): # Two-argument range function
        # Accumulator pattern: accumulation step
        # Note that the accumulation is done with multiplication this time!
        product = product * i

    # Print the result
    print(product)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)