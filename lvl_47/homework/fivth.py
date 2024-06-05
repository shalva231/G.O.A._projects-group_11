def find_second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Example usage:
arr = [5, 10, 3, 8, 9]
print(find_second_largest(arr))


''' 
უარეს შემთხვევაში გაკეთებული შედარებების რაოდენობა არის 2𝑁 − 3
2N − 3, სადაც N არის ელემენტების რაოდენობა სიაში.
'''