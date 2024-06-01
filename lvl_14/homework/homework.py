'''
დავალება1) შექმენით სია, 
რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე), 
ბოლოს დაპრინტეთ მთლიანი სია.
Create an array which will include numbers from 0 to 20 
(write it manually, without loops), then print whole array.
'''

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(numbers)



'''
დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
Create a new array, which will include even numbers from the first array. Then print this new array.
'''

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_nums = []
# for i in numbers:
#     if i % 2 == 0:
#         even_nums.append(i)

# print(even_nums)


'''
დავალება3) შექმენით ახალი სია, 
შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). 
ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
Create an array, 
then add numbers from 50 to 100 to it. In the end, 
print the part of this array with negatives indexes.
'''

# numbers = []
# for i in range(50,100+1):
#     numbers.append(i)

# print(numbers[-20:])


'''
დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი,
შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის, 
ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. 
ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.
Ask user for two inputs and store them as variables, t
heir type has to be int. Then use for loop,
use lower number from this two variables as start, 
Higher number as end, you do not need step. After that, 
you'll have to use if statement to only print multiples of five.
'''

# start = int(input("Enter an integers: "))
# end = int(input("Enter an integers: "))

# for i in range(start, end + 1):
#     if i % 5 == 0:
#         print(i)


'''
დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, 
შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.
Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. 
Then add this name to already created array and print it.
'''

# name = []
# age = input("Enter your age: ")
# if int(age) > 18:
#     user_name = input("Enter your name: ")
#     name.append(user_name)
# print(name)
