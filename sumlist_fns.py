# Sum a list, using the accumulator pattern
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def readNumList() -> List[float]:
    """REad a list of numbers from the keyboard, and return the list."""
    # Accumulator variable
    numlist:List[float] = []
    # Find out how many numbers to read
    numnums:int = int(input('How many numbers should I read? '))
    # In a loop, accumulate the answer
    for i in range(numnums):
        # Ask for a number
        num:float = float(input('Please enter a number for the sum: '))
        numlist.append(num)
    return numlist

def sumlist(numberList:List[float]) -> float:
    """Sum the given numberList, and return that sum."""
    # Initialize the accumulator variable
    nsum:float = 0
    for num in numberList:
        nsum += num
    return nsum

def main(args:List[str]) -> int:
    """Sum a list of numbers, read from the 
    keyboard."""
    list_of_nums:List[float] = readNumList()
    sum_of_list:float = sumlist(list_of_nums)

    # Print out the sum
    print('The sum of the numbers you entered is:', sum_of_list)

    # Print out the average
    print('The average of the numbers you entered is:', (sum_of_list/len(list_of_nums)))

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv) 