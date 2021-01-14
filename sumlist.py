# Sum a list, using the accumulator pattern
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def main(args:List[str]) -> int:
    """Sum a list of numbers, read from the keyboard."""
    # Initialize the accumulator variable
    nsum:float = 0
    # Find out how many numbers to read
    numnums:int = int(input('How many numbers should I read? '))
    # In a loop, accumulate the answer
    for i in range(numnums):
        # Ask for a number
        num:float = float(input('Please enter a number for the sum: '))
        # Add it into the sum (accumulate)
        nsum = nsum + num

    # Print out the sum
    print('The sum of the numbers you entered is:', nsum)

    # Print out the average
    print('The average of the numbers you entered is:', (nsum/numnums))

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv) 