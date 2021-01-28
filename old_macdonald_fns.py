# Print the lyrics to "Old Macdonald", using a function
# Peter Brown <peter.brown@converse.edu>, 2021-01-25

from typing import List

def article(word:str) -> str:
    """Takes a word and returns the correct article ("a" or "an")
    to use with that article."""
    art:str = 'a'
    # 'Y' is so seldom a beginning vowel in English that we'll ignore it
    if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        art = 'an'
    return art

def printVerse(animals:str, sound:str) -> None:
    art:str = article(sound)
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print('And on that farm he had some {0}, E-I-E-I-O!'.format(animals))
    print('With {1} {0}, {0} here and {1} {0}, {0} there,'.format(sound, art))
    print('Here {1} {0}, there {1} {0}, everywhere {1} {0}, {0},'.format(sound, art))
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