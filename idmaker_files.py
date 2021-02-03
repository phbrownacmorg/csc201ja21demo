# Make a Converse-style ID from a name
# Peter Brown <peter.brown@converse.edu>, 2021-01-21

from typing import List, Tuple

def read_input(infilename:str) -> List[str]:
    with open(infilename, 'r') as f:
        return f.readlines()[:]

def write_output(outfilename:str, records:List[str]) -> None:
    with open(outfilename, 'w') as f:
        f.write('userid\tlastname\tfirstname\tmiddlename\n')
        for r in records:
            f.write(r + '\n')

def id_from_line(inputline:str) -> str:
    namelist:List[str] = inputline.strip().split('\t')
    #print(namelist)
    # Strip out extraneous spaces
    for i in range(len(namelist)):
        namelist[i] = namelist[i].strip()
    firstname:str = namelist[1]
    middlename:str = ''
    if len(namelist) > 2: # If there *is* a middle name  
        middlename = namelist[2]

    # Strip suffix off last name
    suffixes:Tuple[str,...] = ('Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'VI')
    lastnamelist:List[str] = namelist[0].split(',')
    if len(lastnamelist) == 1: # Comma didn't split anything, try a space
        lastnamelist = namelist[0].split(' ')
    #print(lastnamelist)
    if len(lastnamelist) > 1 and lastnamelist[-1].strip() in suffixes:
        lastnamelist = lastnamelist[:-1]
    lastname:str = ''.join(lastnamelist).replace("'", '').replace(' ','')

    # Figure out the userid
    if len(middlename) > 0:
	    userid:str = (firstname[0] + middlename[0] + lastname + '001').lower()
    else:
	    userid = (firstname[0] + lastname + '001').lower()
    return userid + '\t' + '\t'.join(namelist)

def main(args:List[str]) -> int:
    infilename:str = 'names.csv'
    outfilename:str = 'userids.csv'

    inputlines:List[str] = read_input(infilename)
    outrecords:List[str] = []
    for line in inputlines[1:]: # type: str
        outrecords.append(id_from_line(line))
    write_output(outfilename, outrecords)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)