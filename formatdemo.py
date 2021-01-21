# Demonstrate the string format() method
# Peter Brown <peter.brown@converse.edu>, 2021-01-21

from typing import List, Tuple
from datetime import date

def main(args:List[str]) -> int:
    # Phone number
    phone:str = '8648675309'
    areacode:str = phone[:3]
    exchange:str = phone[3:6]
    number:str = phone[6:]
    print('{0}-{1}-{2}'.format(areacode, exchange, number))
    print('{0}.{1}.{2}'.format(areacode, exchange, number))
    print('({0}) {1}-{2}'.format(areacode, exchange, number))
    
    # SSN
    ssn:str = '123456789'
    print('{0}-{1}-{2}'.format(ssn[:3], ssn[3:5], ssn[5:]))

    # Dates
    today:date = date.today()
    print(today.year, today.month, today.day)
    month_abbrs:Tuple[str] = ('', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    # Two-digit year
    # Usual American format (two-digit year)
    print('{0}/{1}/{2}'.format(today.month, today.day, today.year % 100))
    # Usual British format (two-digit year)
    print('{1}/{0}/{2}'.format(today.month, today.day, today.year % 100))
    # Usual German/Dutch format (two-digit year)
    print('{1}.{0}.{2}'.format(today.month, today.day, today.year % 100))
    # DOS format
    print('{1}-{0}-{2:02d}'.format(month_abbrs[today.month], today.day, today.year % 100))

    # Four-digit year
    # Usual American format (four-digit year)
    print('{0}/{1}/{2}'.format(today.month, today.day, today.year))
    # Usual British format (four-digit year)
    print('{1}/{0}/{2}'.format(today.month, today.day, today.year))
    # ISO 8601 format
    print('{2}-{0:02d}-{1:02d}'.format(today.month, today.day, today.year))

    # With month abbreviations
    # American
    print('{0}. {1}, {2}'.format(month_abbrs[today.month], today.day, today.year))
    # British
    print('{1} {0}. {2}'.format(month_abbrs[today.month], today.day, today.year))

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)