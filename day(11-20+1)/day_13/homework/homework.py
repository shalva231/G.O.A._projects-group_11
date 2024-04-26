'''
2)  Calculate the sum of all even numbers from 1 to 10 using a while loop:
'''

# num = 1
# sum = 0
# while num != 10+1:
#     if num % 2 == 0:
#         sum += num
#     num += 1
# print(sum)


'''
3) while ციკლის მეშვეობით შეამოწმეთ რიცხვები 1 დან 20 ჩათვლით, 
რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტეთ ეგ რიცხვი
'''

# num = 1

# while num != 20+1:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)
#     num += 1


'''
4) for ციკლის მეშვეობით დაბეჭდეთ ყველა რიცხვი 1-100 ჩათვლით რომელიც იყოფა 5 ზე
'''

# for i in range(1,100+1):
#     if i % 5 == 0:
#         print(i)

'''
5) for ციკლის მეშვეობით დაბეწეთ ყველა ის ირცხვი რომელიც იყოფა 6_ზე 1 დან 20 ის ჩათვლით
'''

# for i in range(1,20+1):
#     if i % 6 == 0:
#         print(i)

'''
==========================================
'''

'''
1) Write a program that takes an input from the user and checks if it's a positive, 
negative, 
or zero number using if-else.
'''

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("even")
# elif num % 2 != 0:
#     print("odd")
# else:
#     print("zero")

'''
2)Write a program that prints all the even numbers between 1 and 20 using a for loop and if statement.
'''

# for i in range(1,20+1):
#     if i % 2 == 0:
#         print(i)

'''
3)Write a program that calculates the sum of a number entered by the user using a while loop.
'''
# sum = 0
# num = int(input("Enter a number (input 0 to calculate the sum): "))
# while num != 0:
#     num = int(input("Enter a number (input 0 to calculate the sum): "))
#     sum += num
# print(sum)

'''
4)Write a program that simulates a basic ATM. It should ask the user for their PIN, 
and if it's correct, display a text withdrawal, deposit, and balance. 
'''

# pin = int(input("Enter your pin: "))

# while pin != 1234:
#     pin = int(input("Enter your pin: "))


# print("withdrawal")
# print("deposit")
# print("balance")


'''
5)Write a program that simulates a simple login system. Ask the user for a username and password, 
and if they enter "admin" and "password123", respectively, print "Login successful" using if-else.
'''

# username = input("Enter your username: ")
# password = int("enter your password: ")

# while username != "admin" and password != "password123":
#     username = input("Enter your username: ")
#     password = int("enter your password: ")

# print("Login successful")


'''
6) Write a program that asks the user for their age and prints a message based on the age range 
(e.g., "Child", "Teenager", "Adult") using if-elif-else.
'''

# age = int(input("Enter your age: "))

# if age <= 12:
#     print("Child")

# elif 13 < age <= 19:
#     print("Teenager")

# else:
#     print("Adult")
