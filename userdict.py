# Create a dictionary with information about users
# Peter Brown <peter.brown@converse.edu>, 2021-02-02

from datetime import date
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
            #print(persondict)
    return result

def years_elapsed(date1:date, date2:date) -> int:
    # Assume date2 > date1
    year1:int = date1.year
    year2:int = date2.year
    result:int = year2 - year1
    # is date2 earlier in the year than date1?
    date3:date = date(year1, date2.month, date2.day)
    if date3 < date1: # Haven't reached the birthday yet
        result = result - 1
    return result

def add_ages(users:dict) -> None:
    for id in users.keys():
        userval:dict = users[id]
        if 'birthdate' in userval:
            birthdate:date = date.fromisoformat(userval['birthdate'])
            #print(date.today() - birthdate)
            #print(years_elapsed(birthdate, date.today()))
            userval['age'] = years_elapsed(birthdate, date.today())

def main(args:List[str]) -> int:
    userdict:dict = dict_from_file('userids.csv')
    add_ages(userdict)
    print(userdict)
    return 0 

if __name__ == "__main__":
    import sys    
    main(sys.argv)