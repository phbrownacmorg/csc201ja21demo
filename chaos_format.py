# A simple program illustrating chaotic behavior
# Peter Brown <peter.brown@converse.edu>, 2020-01-11

from typing import List

def main(args:List[str]) -> int:
    # Establish minimum and maximum initial values
    minval:float = 0.00000001
    maxval:float = 1 - minval

    print('This program illustrates a chaotic function.')
    x:float = float(input('Enter a number between 0 and 1: '))
    
    # Clamp x to the acceptable range
    x = max(minval, x)  # Force x >= minval
    x = min(maxval, x)  # Force x <= maxval
    
    # Print table headers
    print('{0:>2}    {1:^14}'.format('i', 'x'))
    print('-' * 20)

    for i in range(10): # type: int
        x = 3.9 * x * (1 - x)
        print('{0:>2}    {1:.12f}'.format(i, x))
    
    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)