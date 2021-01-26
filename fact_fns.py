# Find a factorial using the accumulator pattern
# Peter Brown <peter.brown@converse.edu>, 2021-01-13

from typing import List

def fact(n:int) -> int:
    """Calculate and return the factorial of the given number n."""
    # Accumulator pattern: initialize the accumulator variable
    product:int = 1 # (identity element for multiplication)

    for i in range(1,n+1): # Two-argument range function
        # Accumulator pattern: accumulation step
        product = product * i
    return product


def main(args:List[str]) -> int:
    """Find a factorial using the accumulator pattern."""
    # Get the number for the factorial.
    n:int = int(input('Please enter a positive integer: '))
    print(str(n) + '! = ', end='')

    # Print the result
    print(fact(n))

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)