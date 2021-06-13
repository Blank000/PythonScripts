import sys

def validate_and_return_sum(args):
    '''
        Number of arguments must be three, if not intimate the user and exit the application
    '''
    if len(args) != 4:
        return "Exactly 3 numbers are required"
    else:
        '''
            Verifying each command line argument must be a integer or else will intimate the user and exit the application
        '''
        try:
            a = int(args[1])
            b = int(args[2])
            c = int(args[3])

        except ValueError:
            return "All inputs must be numeric"

        # Below is the list of numbers whcih values are counted as 0
        teen = [13, 14, 17, 18, 19]

        # Checking if the values lie in the list `teen`, If True then changing their values to 0
        a = 0 if a in teen else a
        b = 0 if b in teen else b
        c = 0 if c in teen else c

        return a+b+c

if __name__ == "__main__":
    print(validate_and_return_sum(sys.argv))