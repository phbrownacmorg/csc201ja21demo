# Print the lyrics to "Old Macdonald", using a function
# Peter Brown <peter.brown@converse.edu>, 2021-01-25

from typing import List

def printVerse(animals:str, sound:str) -> None:
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print('And on that farm he had some {0}, E-I-E-I-O!'.format(animals))
    print('With a {0}, {0} here and a {0}, {0} there,'.format(sound))
    print('Here a {0}, there a {0}, everywhere a {0}, {0},'.format(sound))
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print()


def main(args:List[str]) -> int:

    printVerse('cows', 'moo')
    printVerse('ducks', 'quack')
    printVerse('sheep', 'baa')
    printVerse('horses', 'neigh')
    printVerse('chickens', 'cluck')
    printVerse('dogs', 'woof')
    printVerse('cats', 'meow')
    printVerse('pigs', 'oink')
    
    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)