# Read a year from the keyboard, and determine whether it's a leap year
# Peter Brown <peter.brown@converse.edu>, 2021-01-28

from typing import List

# Boolean function
def isLeapYear(year:int) -> bool:
    """Takes a year and returns a bool telling whether the year is a leap year."""
    isLeap:bool = (year % 4 == 0 and year % 100 != 0) \
                    or (year % 400 == 0)

    # isLeap:bool = False
    # if year % 400 == 0:
    #     isLeap = True
    # elif year % 100 == 0:
    #     isLeap = False
    # elif year % 4 == 0:
    #     isLeap = True

    # if year % 4 == 0:
    #     isLeap = True
    # # Gregorian century-year logic
    # if year % 100 == 0:
    #     isLeap = False
    # if year % 400 == 0:
    #     isLeap = True
    return isLeap

def main(args:List[str]) -> int:
    year:int = int(input('Please enter a year: '))

    print('{} is '.format(year), end='')
    if not isLeapYear(year):
        print ('NOT', end=' ')
    print('a leap year.')

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)