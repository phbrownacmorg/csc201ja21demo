# Create a dictionary with information about users
# Peter Brown <peter.brown@converse.edu>, 2021-02-02

from typing import List

def dict_from_file(fname:str) -> dict:
    """Read a dictionary from a TSV file.  The first column is used as the key."""
    result:dict = dict()
    with open(fname, 'r') as f:
        # Handle the header line differently
        fields:List[str] = f.readline().strip().split('\t')
        #print(fields)
        for line in f.readlines():
            values:List[str] = line.strip().split('\t')
            #print(values)
            key:str = values[0]
            persondict = dict()
            for i in range(len(values)):
                persondict[fields[i]] = values[i]
            result[key] = persondict
            print(persondict)
    return result

def main(args:List[str]) -> int:
    userdict:dict = dict_from_file('userids.csv')
    print(userdict)
    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)