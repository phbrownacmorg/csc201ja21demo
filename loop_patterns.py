# Do nothing, successfully
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def interactive_loop() -> None:
    """Interactive loop.  Stay in the loop until the user says to quit.  (Yes, this example is also a sentinel loop.)"""
    nums:List[float] = []
    inStr:str = input('Please enter a number, or "Q" to quit: ')
    while inStr.upper().strip() != 'Q':
        thisNum:float = float(inStr)
        nums.append(thisNum)
        print('Entered so far:', nums)
        print('Sum:', sum(nums), 'Average:', sum(nums)/len(nums))
        inStr = input('Please enter a number, or "Q" to quit: ')
    print('Goodbye!')

def sentinel_loop() -> None:
    """A sentinel loop keeps taking data until it sees a particular funny value.  (Yes, this example is also an interactive loop.)"""
    sentinel:float = -99999
    nums:List[float] = []
    this_num:float = float(input('Please enter a number, or {} to quit: '.format(sentinel)))
    while this_num != sentinel:
        nums.append(this_num)
        print('Entered so far:', nums)
        print('Sum:', sum(nums), 'Average:', sum(nums)/len(nums))
        this_num = float(input('Please enter a number, or {} to quit: '.format(sentinel)))
    print('Goodbye!')

def sentinel_loop_empty_sentinel() -> None:
    """Sentinel loop, using the empty string as the sentinel."""
    nums:List[float] = []
    inStr:str = input('Please enter a number, or hit Enter to quit: ')
    while inStr.strip() != '':
        thisNum:float = float(inStr)
        nums.append(thisNum)
        print('Entered so far:', nums)
        print('Sum:', sum(nums), 'Average:', sum(nums)/len(nums))
        inStr = input('Please enter a number, or hit Enter to quit: ')
    print('Goodbye!')

def file_loop(infile:str) -> None:
    """Read from a file, using the end of file as the sentinel.  This is *not* an interactive loop."""
    with open(infile, 'r') as f:
        line:str = f.readline()
        while line.strip() != '':
            print(line.strip())
            line = f.readline()
    print('Goodbye!')

def nested_loops(infile:str) -> None:
    """Read from a file, using the end of file as the sentinel.  This is *not* an interactive loop."""
    numsum:float = 0
    num_count:int = 0
    with open(infile, 'r') as f:
        line:str = f.readline() # Get rid of column headers
        line = f.readline()
        while line.strip() != '':
            numbers:List[str] = line.split(',')
            for num in numbers: # type: str
                numsum += float(num.strip())
                num_count += 1
            line = f.readline()
    print('Read ', num_count, 'numbers, with a sum of ', numsum, 'and an average of', numsum/num_count)
    print('Goodbye!')

def main(args:List[str]) -> int:
    interactive_loop()
    sentinel_loop()
    sentinel_loop_empty_sentinel()
    file_loop('chaos-in.csv')
    nested_loops('chaos-in.csv')
    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)