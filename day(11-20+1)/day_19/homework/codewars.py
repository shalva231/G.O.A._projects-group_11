'''
1
Find the smallest integer in the array
'''
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

'''
2
Remove String Spaces
'''
def no_space(x):
    return x.replace(" ", "")

'''
3
Convert a Boolean to a String
'''
def boolean_to_string(b):
    return str(b)

'''
4
Sum Arrays
'''
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

'''
5
Abbreviate a Two Word Name
'''
def abbrev_name(name):
    index = name.index(" ")
    return f"{name[0].upper()}.{name[index+1].upper()}"

'''
6
Beginner - Lost Without a Map
'''
def maps(a):
    dub = []
    for i in a:
        dub.append(i * 2)
    return dub

'''
7
MakeUpperCase
'''
def make_upper_case(s):
    upper = ""
    for i in s:
        upper += i.upper()
    return(upper)


'''
8
Calculate average
'''
def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return sum(numbers) / len(numbers)


'''
9
Calculate BMI
'''
def bmi(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        return"Underweight"

    if BMI <= 25.0:
        return "Normal"

    if BMI <= 30.0:
        return "Overweight"

    if BMI > 30:
        return "Obese"