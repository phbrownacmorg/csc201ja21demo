# Determine whether a date is a valid Gregorian date
# Peter Brown <peter.brown@converse.edu>, 2021-01-28

from typing import List, Optional, Tuple
from leapyear import isLeapYear

def parseDateString(dateStr:str) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    month:Optional[int] = None
    day:Optional[int] = None
    year:Optional[int] = None
    dateparts:List[str] = dateStr.split('/')
    #print(dateparts)
    if len(dateparts) == 3:
        month = int(dateparts[0].strip())
        day = int(dateparts[1].strip())
        year = int(dateparts[2].strip())
    return month, day, year

def validYear(year:int) -> bool:
    return year >= 1582   # Future years are OK

def validMonth(month:int) -> bool:
    return 1 <= month <= 12

def validDay(month:int, day:int, year:int) -> bool:
    valid:bool = True
    if day < 1 or day > 31:
        valid = False
    # 30-day months
    elif month in (9, 4, 6, 11) and day == 31: 
        valid = False
    # February
    elif month == 2 and day > 29:
        valid = False
    elif month == 2 and day == 29 and not isLeapYear(year):
        valid = False
    return valid

 

def main(args:List[str]) -> int:
    # Read a date from the keyboard
    dateStr:str = input('Please enter a date (m/d/yyyy, 4-digit year): ')

    print('{} is '.format(dateStr), end='')
    if not validDate(dateStr):
        print ('NOT', end=' ')
    print('a valid Gregorian date.')


    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)