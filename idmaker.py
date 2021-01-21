# Make a Converse-style ID from a name
# Peter Brown <peter.brown@converse.edu>, 2021-01-21

from typing import List

def main(args:List[str]) -> int:
    # Get the name
    # Entering last-name first handles spaces, etc., in last names
    name:str = input('Please enter your full name, last name first: ')

    # Figure out the ID

    namelist:List[str] = name.split(',')
    print(namelist)
    # Split first and middle names on the spaces.
    # This doesn't always do the right thing with Southern double names.
    namelist[1:] = namelist[1].split()
    print(namelist)
    
    firstname:str = namelist[1].lower()
    # Doesn't handle people with no middle name.  
    middlename:str = namelist[2].lower()
    lastname:str = namelist[0].lower().replace(' ', '').replace("'", '')
    
    # Put the name back together, in its proper order
    name = ' '.join(namelist[1:]) + ' ' + namelist[0]

    print(name, ', your ID is: ', sep='', end='')
    id:str = firstname[0] + middlename[0] + lastname + '001'
    print(id)

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)