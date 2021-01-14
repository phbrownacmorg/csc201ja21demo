# Convert pounds to stone
# Peter Brown <peter.brown@converse.edu>, 2020-01-12

from typing import List

def main(args:List[str]) -> int:
    # Get the weight in pounds
    lbs:float = float(input('Please enter a weight in pounds: '))
    print(lbs, 'pounds = ', end='')
    # Convert it to stone
    st:float = lbs/14
    # Output the result
    print(st, 'stone')

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)