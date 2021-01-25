# Make a Converse-style ID from a name
# Peter Brown <peter.brown@converse.edu>, 2021-01-21

from typing import List

def main(args:List[str]) -> int:
    infilename:str = 'names.csv'
    outfilename:str = 'userids.csv'

    with open(outfilename, 'w') as out_f:
        # Print column headers
        out_f.write('userid,lastname,firstname,middlename\n')
        with open(infilename, 'r') as f_in:
            # Skip the column headers
            for line in f_in.readlines()[1:]:
                namelist:List[str] = line.split(',')
                #print(namelist)
                # Strip out extraneous spaces
                for i in range(len(namelist)):
                    namelist[i] = namelist[i].strip()
                firstname:str = namelist[1]
                # Doesn't (yet) handle people with no middle name.  
                middlename:str = namelist[2]
                lastname:str = namelist[0].replace(' ', '').replace("'", '')
        
                # Figure out the userid
                userid:str = (firstname[0] + middlename[0] + lastname + '001').lower()
                # Output the userid with the name
                out_f.write(userid + ',' + ','.join(namelist) + '\n')

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)