# Calculate the future value of an investment
# Peter Brown <peter.brown@converse.edu>, 2021-01-12

from typing import List

def main(args:List[str]) -> int:
    # Read from the keyboard: amount, interest rate, periods
    # read the amount (principal)
    # This is the accumulator variable (accumulator pattern)
    P:float = float(input('Please enter the amount to invest: $'))
    rate:float = float(input('Please enter the interest rate per period, with no %: '))
    periods:int = int(input('Please enter the number of periods: '))
    # Print out the initial parameters
    print('Investing $', P, 'at', rate, "% for", periods, 'periods.')
    # Adjust the rate from a percentage to a raw number
    rate = rate/100

    # Calculate and print out the investment table
    # Print a header row
    print('Period\tInterest\tAmount')
    # Print the starting amount
    print('Initial\t\t\t\t$', round(P,2))
    # Print out the table, row by row
    for i in range(periods):
        # Calculate the interest
        interest = P * rate
        # Add the interest back into the principal (accumulate)
        P = P + interest
        # Print the table row
        print((i+1), '\t\t$', round(interest,2), '\t\t$', round(P,2))

    return 0

if __name__=='__main__':
    import sys
    main(sys.argv)
