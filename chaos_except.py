# A simple program illustrating chaotic behavior
# Peter Brown <peter.brown@converse.edu>, 2020-02-01

from typing import List

def main(args:List[str]) -> int:
    print('This program illustrates a chaotic function.')
    # Danger here
    inputStr:str = input('Enter a number between 0 and 1: ')
    try:
        x:float = float(inputStr)
    except ValueError:
        print('"{}" is not a number.'.format(inputStr))
    else:
        if x < 0 or x > 1:
            print('"{}" is not between 0 and 1.'.format(inputStr))
        else:
            # Print table headers
            print('{0:^4}\t{1:^14}'.format('i', 'x'))
            print('-' * 22)

            print('Seed\t{0:.12f}'.format(x))
            for i in range(10): # type: int
                x = 3.9 * x * (1 - x)
                print('{0:^4}\t{1:.12f}'.format(i+1, x))
    
    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)