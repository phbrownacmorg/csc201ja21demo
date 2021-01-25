# A simple program illustrating chaotic behavior
# Peter Brown <peter.brown@converse.edu>, 2020-01-11

from typing import List

def main(args:List[str]) -> int:
    # Establish minimum and maximum initial values
    minval:float = 0.00000001
    maxval:float = 1 - minval

    #print('This program illustrates a chaotic function.')
    infilename:str = 'chaos-in.csv'
    outfilename:str = 'chaos-out.txt'

    with open(infilename, 'r') as infile:
        with open(outfilename, 'w') as outfile:
            # Skip the first line
            for line in infile.readlines()[1:]: # type:str
                invals:List[str] = line.split(',')
                x:float = float(invals[0])
                n:int = int(invals[1])

                # Clamp x to the acceptable range   
                x = max(minval, x)  # Force x >= minval
                x = min(maxval, x)  # Force x <= maxval

                # Print table headers
                outfile.write('n = {}\tx = {}\n'.format(n, x))
                outfile.write('{0:>2}    {1:^14}\n'.format('i', 'x'))
                outfile.write('-' * 20 + '\n')

                for i in range(n): # type: int
                    x = 3.9 * x * (1 - x)
                    outfile.write('{0:>2}    {1:.12f}\n'.format(i, x))
                outfile.write('\n')
    
    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)