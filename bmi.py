# BMI classification
# Peter Brown <peter.brown@converse.edu>, 2021-01-27

from typing import List

def bmi(inches:float, pounds:float) -> float:
    return (pounds / inches**2) * 703

def classify(bmi:float) -> str:
    result:str = ''
    if bmi < 15:
        result = 'very severely underweight'
    elif bmi < 16:
        result = 'severely underweight'
    elif bmi < 18.5:
        result = 'underweight'
    elif bmi < 25:
        result = 'normal'
    elif bmi < 30:
        result = 'overweight'
    elif bmi < 35:
        result = 'moderately obese'
    elif bmi < 40:
        result = 'severely obese'
    else:
        result = 'very severely obese'

    return result
    

def main(args:List[str]) -> int:
    # Ask for height in inches and weight in pounds
    height:float = float(input("Please enter a person's height in inches: "))
    weight:float = float(input("Please enter this person's weight in pounds: "))

    # Find and classify BMI
    classification:str = classify(bmi(height, weight))
    # Print results
    print("This person has a BMI of {:.1f}".format(bmi(height, weight)))
    print('That BMI is considered ' + classification + '.')
    return 0

if __name__ == "__main__":
    import sys    
    main(sys.argv)