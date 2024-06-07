# This function calculates the sum of the two smallest numbers in a given list of numbers.

def sum_two_smallest_numbers(numbers):
    # Initialize an empty list to store the smallest numbers.
    smallest = []
    # Assume the first number in the list is the smallest.
    small = numbers[0]
    # Iterate through the list of numbers.
    for i in numbers:
        # If a smaller number is found, update the smallest value.
        if i < small:
            small = i

    # Add the smallest number to the list.
    smallest.append(small)
    # Remove the smallest number from the original list.
    numbers.remove(small)
    # Reset the smallest value to the first number in the updated list.
    small = numbers[0]

    # Repeat the process to find the second smallest number.
    for i in numbers:
        if i < small:
            small = i
    
    # Add the second smallest number to the list.
    smallest.append(small)
    # Return the sum of the smallest numbers.
    return sum(smallest)