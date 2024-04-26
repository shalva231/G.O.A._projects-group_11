'''
Write a program that takes asks user for number (use input). 
If number is even, print that number is even.
Else print that number is not even, 
also print next even number, 
for example if input is 15, print 16.
'''

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even.")
#     next_even_number = number + 1
#     print(f"The next even number is {next_even_number}.")
# else:
#     print(f"{number} is not even.")



'''
Create a while loop that asks the user to enter a password. 
Keep asking until they enter the correct password "Goa best". 
Also print the count of incorrect passwords.
'''

# password = ""
# incorrect_password_count = 0

# while password!= "Goa best":
#     password = input("Enter the password: ")
#     incorrect_password_count += 1

# print(f"You entered an incorrect password {incorrect_password_count} times.")


'''
Write an algorithm that takes a string as input 
and returns True if first character of that string is "G".
'''

# string = input("please enter a text here -> ")

# if string[0] == "G":
#     print(True)
# else:
#     print(False)

'''
Ask user for five names (use input five times). 
Add all of them in one list and print only first three names.
'''

# names = []

# for i in range(5):
#     name = input(f"Enter name {i+1}: ")
#     names.append(name)

# print(f"The first three names are {names[0]}, {names[1]}, and {names[2]}.")


'''
Write an algorithm that checks if a given number is prime or not 
(prime number has only two divisors - გამყოფი) 
Use a for loop for this task.
'''

# num = int(input("please enter a numebr: "))

# for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num}, is not a prime number")
#             break

'''
Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე)..
'''

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

'''
Implement a simple calculator that takes two numbers and an operator 
(+, -, *, /) as input from the user and performs the corresponding operation. 
Bonus task if you want, 
it's not necessary - add degree (ხარისხი), use ** operator for it.
'''


# operators = ["+", "-", "*", "/"]

# while True:
#     num1 = float(input("Enter the first number: "))
#     operator = input("Enter the operation: ")
#     num2 = float(input("Enter the second number: "))

#     if operator not in operators:
#         print("Invalid operator.")
#         continue

#     result = 0
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         result = num1 / num2

#     print(f"{num1} {operator} {num2} = {result}")

#     continue_operation = input("Do you want to continue? (y/n): ")
#     if continue_operation.lower() == "n":
#         break



'''
Ask user to enter name and print the last character of that string.
'''

# name = input("Enter your name: ")
# print(f"The last character of your name is {name[-1]}.")



'''
Using for loop, ask user for number. 
Then create a list which will have even numbers in next range: 
from 0 to user's number. At last, print out whole list. 
'''

# number = int(input("Enter a number: "))
# even_numbers = []

# for i in range(number + 1):
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)



'''
Ask user for whole number. 
Then create a factorial for this number and print it out 
(If you don't know what a factorial is, google it). 
'''

# number = int(input("Enter a whole number: "))
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print(f"The factorial of {number} is {factorial}.")
