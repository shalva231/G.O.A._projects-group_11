# This function finds the largest multiple of a given divisor within a specified bound.
def max_multiple(divisor, bound):
    # Initialize an empty list to store the multiples of the divisor.
    multiples = []
    # Iterate through numbers from 1 to the given bound (inclusive).
    for n in range(1, bound + 1):
        # Check if the current number is a multiple of the divisor.
        if n % divisor == 0:
            # If it is, add it to the list of multiples.
            multiples.append(n)
            
    # After iterating through all numbers, return the maximum value from the list of multiples.
    return max(multiples)