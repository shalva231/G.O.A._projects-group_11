# # Program to print numbers from 1 to 10 using a while loop

# i = 1
# while i <= 10:
#     print(i)
#     i += 1



# # Program to print the even numbers from 1 to 10 using a for loop

# for i in range(2, 11, 2):
#     print(i)



# # Program to ask the user to enter a number and print whether it is positive, negative, or zero

# number = int(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



# # Program to ask the user to enter a password and check whether it is correct

# password = input("Enter a password: ")
# if password == "abc123":
#     print("Access granted")
# else:
#     print("Access denied")



# # Program to print numbers from 1 to 10, stopping if the number is 5 using a while loop and the break statement

# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1



# # Program to ask the user to enter a number between 1 and 5 and print whether it is valid

# while True:
#     number = int(input("Enter a number between 1 and 5: "))
#     if number >= 1 and number <= 5:
#         print("Valid input")
#         break
#     else:
#         print("Invalid input")



# # Program to ask the user to enter a number and check whether it is divisible by 3, 5, or both 3 and 5

# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)