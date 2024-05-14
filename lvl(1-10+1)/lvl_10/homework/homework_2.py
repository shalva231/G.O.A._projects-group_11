# Examples using range():

# Example 1: Print numbers from 0 to 9
for i in range(10):
    print(i)

# Example 2: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Example 3: Print even numbers from 0 to 9
for i in range(0, 10, 2):
    print(i)

# Example 4: Print odd numbers from 1 to 9
for i in range(1, 10, 2):
    print(i)

# Example 5: Print numbers from 10 to 1 in reverse order
for i in range(10, 0, -1):
    print(i)

# Example 6: Generate a list of squares of numbers from 1 to 10
squares = [i ** 2 for i in range(1, 11)]
print(squares)

# Example 7: Use range() to iterate over indices of a list
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i])

# Example 8: Sum of numbers from 1 to 10 using range()
total = sum(range(1, 11))
print(total)

# Example 9: Iterate over a range and print multiples of 3
for i in range(3, 31, 3):
    print(i)

# Example 10: Generate a list of characters from 'a' to 'j'
characters = [chr(i) for i in range(97, 107)]
print(characters)


# Examples using for loop:

# Example 1: Iterate over a list of strings
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 2: Iterate over a tuple of numbers
tuple_nums = (1, 2, 3, 4, 5)
for num in tuple_nums:
    print(num)

# Example 3: Iterate over a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key, ':', value)

# Example 4: Iterate over a string and print characters
string = "Hello"
for char in string:
    print(char)

# Example 5: Iterate over a set
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(num)

# Example 6: Iterate over a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num)

# Example 7: Iterate over a list with index using enumerate()
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 8: Iterate over a range and print squared values
for i in range(1, 11):
    print(i, i**2)

# Example 9: Iterate over a list in reverse order
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)

# Example 10: Iterate over a list and break the loop when a condition is met
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
    if num == 5:
        break


# Examples using while loop:

# Example 1: Print numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Example 2: Calculate the sum of numbers from 1 to 10 using a while loop
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)

# Example 3: Print even numbers from 0 to 10 using a while loop
i = 0
while i <= 10:
    print(i)
    i += 2

# Example 4: Iterate over a list using a while loop
fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Example 5: Break the loop when a condition is met
i = 0
while True:
    print(i)
    if i == 5:
        break
    i += 1

# Example 6: Continue to the next iteration when a condition is met
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Example 7: Use a while loop to find the first 5 prime numbers
num = 2
count = 0
while count < 5:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

# Example 8: Repeat a task until a condition is met
user_input = ''
while user_input != 'quit':
    user_input = input("Enter 'quit' to exit: ")

# Example 9: Print numbers from 0 to 9 in reverse order using a while loop
i = 9
while i >= 0:
    print(i)
    i -= 1

# Example 10: Use a while loop to countdown from 10 to 1
count = 10
while count > 0:
    print(count)
    count -= 1
