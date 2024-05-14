'''
1)   for loop-ის გამოყენებით დაპრინტეთ 5-ის და 3-ის ჯერადი რიცხვები 1-დან 100-ის ჩათვლით
'''
# for i in range(1,100+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


'''
2)  შექმენით ცარიელი სია. 
მომხმარებელს შეეკითხეთ სახელი და გვარი, 
რომელსაც დაამატებთ თქვენ მიერ შექმნილ სიაში. 
საბოლო შედეგი გამოიტანეთ ტერმინალში
'''
# lst = []
# lst.append(input("please enter your name: "))
# lst.append(input("please enter your lastname: "))
# print(lst)


'''
3)   მომხმარებელს შემოატანიეთ რიცხვი და for loop-ის დახმარებით დაპრინტეთ რიცხვები 1-დან  
მომხმარებლის მიერ შემოტანილი რიცხვის ჩათვლით.
ტერმინალში გამოიტანეთ ამ რიცხვების ჯამი და საშუალო არითმეტიკული
'''

# num = int(input("please enter a number: "))

# sum = 0
# count = 0
# Arithmetic_av = 0

# for i in range(1,num+1):
#     sum += i
#     count += 1

# Arithmetic_av = sum/count

# print(f"the sum of all the numbers from 1 to {num} is {sum}")
# print(f"the Arithmetic avarage of all the numbers from 1 to {num} is {Arithmetic_av}")


'''
4)  შექმენით სია, 
რომელშიც for ციკლის გამოყენებით შეიტანთ ლუწ რიცხვებს 1-დან 50-ის ჩათვლთ. 
შედეგი დაფრინტეთ ტერმინალში
'''
# even = []
# for i in range(1,50+1):
#     if i % 2 == 0:
#         even.append(i)

# print(even)


'''
5)  მომხმარებელს შემოაქვს რიცხვი. შეამოწმეთ არის თუ არა ეს რიცხვი მარტიცი. 
თუ მარტიცია დაუპრინტეთ "თქვენი რიცხვი მარტივია", 
სხვა შემთხვევაში დაუპრინტეთ "თქვენი რიცხვი არ არის მარტივი"
(მარტივი რიცხვი არის ისეთი ნატურალური რიცხვი რომელსაც გააჩნია მხოლოდ ორი გამოყოფი(1 და თავისი თავი))
'''

# num = int(input("please enter a numebr: "))

# if num == 1:
#     print(f"{num}, is not a prime number")

# for i in range(2,10+1):
#     if i == num:
#         break
#     if num % i == 0:
#         print(f"{num}, is not a prime number")
#         break
#     else:
#         print(f"{num} is a prime number")
#         break