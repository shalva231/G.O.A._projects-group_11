'''
შექმენით ფუნქცია სახელად manual_reverse, 
რომელიც მიიღებს დალაგებულ კოლექციას. 
თქვენი დავალებაა,
რომ შეაბრუნოთ ეს კოლექცია და დააბრუნოთ ამ სახით.
'''

# def manual_reverse(arr):
#     return arr[-1::-1]

# print(manual_reverse([1, 2, 3, 4, 5]))

'''
შექმენით ფუნქცია სახელად manual_replace, 
რომელიც მიიღებს სია, ჩასანაცლებელ ელემენტს და იმ ელემენტს, 
რომლითაც უნდა ჩანაცვლდეს. 
თქვენი დავალებაა, რომ დააბრუნოთ ახალი კოლექცია, 
სადაც გექნებათ ჩანაცვლებული ყველა ელემენტი მესამე პარამეტრით.
'''

# def manual_replace(arr,to_replace,to_replace_with):
#     new_list = []
#     for i in arr:
#         if i == to_replace:
#             new_list.append(to_replace_with)
#         else:
#             new_list.append(i)
#     return new_list

# print(manual_replace([10, 11, 10, 11], 10, 20))

'''
შექმენით ფუნქცია სახელად manual_count, 
რომელიც მიიღებს დალაგებულ კოლექციას და დასათვლელ მნიშვნელობას. 
თქვენი დავალებაა, რომ დააბრუნოთ თუ რამდენჯერ გექნებათ დასათვლელი მნიშვნელობა კოლექციაში.
'''

# def manual_count (arr,count_element):
#     count = 0
#     for i in arr:
#         if i == count_element:
#             count += 1
#     return count

# print(manual_count([12, 13, 14, 12, 14, 100], 12))