# Convert Celsius temperatures to Fahrenheit
# Peter Brown <peter.brown@converse.edu>, 2020-01-12

from typing import List

def main(args:List[str]) -> int:
    # Get the Celsius temperature
    degC:float = float(input('Please enter a temperature in Celsius: '))
    print(degC, 'degrees Celsius = ', end='')
    # Convert it to Fahrenheit
    degF:float = (9/5) * degC + 32
    # Output the result
    print(degF, 'degrees Fahrenheit')

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)