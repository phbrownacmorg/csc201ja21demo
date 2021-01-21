# Demonstrate string operations
# Peter Brown <peter.brown@converse.edu>, 2021-01-21

from typing import List

def main(args:List[str]) -> int:
    # input
    s:str = input("Bring me a shrubbery!  I mean, a string: ")
    print('Input was "' + s + '"')

    # String operations
    # Concatenation with +
    print('We are the knights who say ' + '"Ni!"')
    # Repetition with *
    print('"' + 'Ni! ' * (7 % 4), end='') # Integer *expression*
    print(3 * 'Ni! ' + '"') # Before or after the string

    # Length
    s2:str = '"A duck!"'
    print("Length of the string is", len(s2))
    # Print the subscripts, counting up
    for i in range(len(s2)): # type: int
        print('{0:3d}'.format(i), end=' ')
    print()

    # Iterating character by character
    for ch in s2: # type: str
        print('  ' + ch + ' ', end='')
    print()

    # Print the subscripts, counting down
    for i in range(-len(s2), 0):
        print('{0:3d}'.format(i), end=' ')
    print()

    # Slicing
    print(s2[3:6])
    print(s2[:6])
    print(s2[3:])
    print(s2[1:8:2]) # Odd characters only
    print(s2[::2]) # Odd characters only
    print(s2[::-1]) # Backwards

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)