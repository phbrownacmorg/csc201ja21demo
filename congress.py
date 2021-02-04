# Do nothing, successfully
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def eligibleHRep(age:int, cit:int) -> bool:
    return age >= 25 and cit >= 7

def eligibleSenate(age:int, cit:int) -> bool:
    return age >= 30 and cit >= 9

def main(args:List[str]) -> int:
    age:int = int(input("Please input a person's age: "))
    cit:int = int(input("How many years has this person been a U.S. citizen? "))

    print('This person is {0} years old, and has been a U.S. citizen for {1} years.'.format(age, cit))

    print('This person is', end=' ')
    if not eligibleHRep(age, cit):
        print('NOT', end=' ')
    print('eligible to serve in the U.S. House of Representatives.')

    print('This person is', end=' ')
    if not eligibleSenate(age, cit):
        print('NOT', end=' ')
    print('eligible to serve in the U.S. Senate.')

    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)