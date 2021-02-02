# A simple program illustrating chaotic behavior
# Peter Brown <peter.brown@converse.edu>, 2020-02-01

from typing import List
import math

def validateInput(inputStr:str) -> float:
    bogus_initial_value:float = float('nan')
    x:float = bogus_initial_value
    valid:bool = True
    # First: is this a number at all?
    for c in inputStr:
        if not c.isdigit() and c != '.' and c != '-':
            valid = False
            break
    
    # Correct format?
    if inputStr.count('-') > 1 or (inputStr.count('-') > 0 and inputStr[0] != '-'):
        valid = False
    elif inputStr.count('.') > 1:
        valid = False

    if not valid:
        print('"{}" is not a number.'.format(inputStr))
    else:
        x = float(inputStr)
    
        # Second: is it in the right range?
        if x < 0 or x > 1:
            print('"{}" is not between 0 and 1.'.format(inputStr))
            x = float('nan')
    
    return x


def main(args:List[str]) -> int:
    print('This program illustrates a chaotic function.')
    # Danger here
    x:float = validateInput(input('Enter a number between 0 and 1: '))

    if not math.isnan(x):
        # Print table headers
        print('{0:^4}\t{1:^14}'.format('i', 'x'))
        print('-' * 20)

        print('Seed\t{0:.12f}'.format(x))
        for i in range(10): # type: int
            x = 3.9 * x * (1 - x)
            print('{0:^4}\t{1:.12f}'.format(i+1, x))
    
    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)