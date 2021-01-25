# Convert Celsius temperatures to Fahrenheit
# Peter Brown <peter.brown@converse.edu>, 2020-01-25

from typing import List

def readCelsius() -> float:
    """Read a Celsius temperature from the keyboard."""
    return float(input('Please enter a temperature in Celsius: '))

def convert_CtoF(degC:float) -> float:
    """Takes a Celsius temperature degC and returns the Fahrenheith equivalent."""
    return (9/5) * degC + 32

def printResults(degC:float, degF:float) -> None:
    """Takes a Celsius temperature degC, an equivalent Fahrenheit temperature degF, and prints a message about them being equal."""
    print('{0:.1f}\u00b0C = {1:.1f}\u00b0F'.format(degC, degF))

def main(args:List[str]) -> int:
    # Get the Celsius temperature
    degC:float = readCelsius()
    # Convert it to Fahrenheit
    degF:float = convert_CtoF(degC)
    # Output the result
    printResults(degC, degF)

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)