# A simple program illustrating chaotic behavior
# Peter Brown <peter.brown@converse.edu>, 2020-01-11

from typing import List, Tuple

def readInput(infilename:str) -> List[Tuple[float, int]]:
    parsedInput:List[Tuple[float,int]] = []
    try:
        with open(infilename, 'r') as infile:
            # Skip the first line
            for line in infile.readlines()[1:]: # type:str
                invals:List[str] = line.split(',')
                try:
                    x:float = float(invals[0])
                    n:int = int(invals[1])
                except IndexError:
                    print('Error in input file: input line "{}" does not have two numbers.'.format(line.strip()))
                except ValueError:
                    print('Error in input file: value on input line "{}" is not a number.'.format(line.strip()))
                else:
                    parsedInput.append( (x, n) )

    except FileNotFoundError:
        print('File', infilename, 'could not be found.')
    return parsedInput

def doChaos(inputVals:List[Tuple[float, int]], outfilename:str) -> None:
    with open(outfilename, 'w') as outfile:
        for case in inputVals:
            x = case[0]
            n = case[1]

            # Print table headers
            outfile.write('n = {}\tx = {}\n'.format(n, x))
            outfile.write('{0:>2}    {1:^14}\n'.format('i', 'x'))
            outfile.write('-' * 20 + '\n')

            for i in range(n): # type: int
                x = 3.9 * x * (1 - x)
                outfile.write('{0:>2}    {1:.12f}\n'.format(i, x))
            outfile.write('\n')
    

def main(args:List[str]) -> int:
    #print('This program illustrates a chaotic function.')
    infilename:str = 'chaos-in.csv'
    outfilename:str = 'chaos-out.txt'

    inputVals:List[Tuple[float, int]] = readInput(infilename)
    doChaos(inputVals, outfilename)    
    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)