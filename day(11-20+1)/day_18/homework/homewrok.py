'''
შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. 
თქვენ უნდა დააბრუნოთ გაფილტრული სია, 
სადაც უკვე მარტო 4-ის ჯერადები იქნება.
'''
# def multiples_of_4(arr):
#     mult_of_4 = []
#     for i in arr:
#         if i % 4 == 0 and i >= 4:
#             mult_of_4.append(i)
#     return mult_of_4

# print(multiples_of_4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))


'''
შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. 
შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.
'''

# def user_name(name, surname):
#     lst = []
#     lst.append(name)
#     lst.append(surname)
#     return lst
# name = input("enter your name: ")
# surname = input("enter your surname: ")

# print(user_name(name, surname))


'''
მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. 
ეს რიცხვები გადაეცით ფუნქციას, 
for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. 
შემდეგ მოახდინეთ გაფილტვრა, 
ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, 
ახალ სიაში დაამატეთ მისი მეორე ხარისხი, 
ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).
'''

# def get_numbers(start, end):
#     numbers = []
#     for i in range(start, end+1):
#         numbers.append(i)
#     squared_numbers = []
#     root_numbers = []
#     for i in numbers: 
#         if i % 2 == 0:
#             squared_numbers.append(i**2)
#         else:
#             root_numbers.append(i**0.5)
#     return numbers , squared_numbers , root_numbers

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# numbers = get_numbers(start, end)
# print(numbers)

'''
შექმენით ფუნქცია, 
რომელსაც გადასცემთ მომხმარებლის გვარს. 
გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. 
შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - 
მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. 
საბოლოოდ დააბრუნეთ ეს სია.
Bonus (არაა სავალდებულო): 
ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ. 
'''

# def user_surname(surname):
#     surname_list = []

#     for i in surname:
#         surname_list.append(i)

#     even_list = []

#     for i in surname_list:
#         if surname_list.index(i) % 2 == 0:
#             even_list.append(i)
#     even_str = ""
#     for i in even_list:
#         even_str += i
#     return even_str


# print(user_surname(input("please enter your surname: ")))


'''
შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )
'''

# def Arithmetic_average(numbers):
#     sum_of_numbers = 0
#     for num in numbers:
#         sum_of_numbers += num
#     return sum_of_numbers / len(numbers)


'''
შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. 
შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, 
მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.
'''

# def reverse_word(word):
#     reversed_word = ""
#     for index in range(len(word) -1, -1, -1):
#         reversed_word += word[index]
#     return reversed_word


# print(reverse_word(input("Enter a word: ")))

'''
შექმენით ფუნქცია, 
რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას, 
რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები).
'''

# def get_unique_numbers(numbers):
#     unique_numbers = []
#     for num in numbers:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers
