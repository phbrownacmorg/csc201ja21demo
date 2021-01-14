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

    # Clamp the input values to make them at least slightly sensible
    P = max(P, 0.01)          # Force P >= $0.01
    rate = max(rate, 0)       # Force rate >= 0
    periods = max(periods, 1) # Force periods > 0

    # Print out the initial parameters
    print('Investing $' + str(P), 'at', str(rate) + "% for", periods, 'periods.')
    # Adjust the rate from a percentage to a raw number
    rate = rate/100

    # Calculate and print out the investment table
    # Print a header row
    print('Period\tInterest\tAmount')
    # Print the starting amount
    print('Initial\t\t\t\t$' + str(round(P,2)))
    # Print out the table, row by row
    for i in range(periods):
        # Calculate the interest
        interest = P * rate
        # Add the interest back into the principal (accumulate)
        P = P + interest
        # Print the table row
        print((i+1), '\t\t$' + str(round(interest,2)), 
                    '\t\t$' + str(round(P,2)))

    return 0

if __name__ == "__main__":
    import sys   
    main(sys.argv)