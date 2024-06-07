def calculate_avarage(numbers):
    sum = 0
    count = 0
    for i in numbers:
        sum += i
        count += 1
    return sum / count

print(calculate_avarage([1,2,3,4,5,6,7,8,9,0,1,23,4]))

'''
my algorithms
1.initialises 2 variables
    1.sum = 0
    2.count = 0
2.iterates over the numbers list
    N times
3.it grants numbers values N times
    1.it adds the numbers to the sum variable]
    2.it adds 1 to the count variable
4.and lastly it uses mathematic opperator called division
    1.it divides the sum variable by the count variable
    2.it returns the result
'''

'''
my algorithm does 
initialisation - 2 times
1.sum = 0
2.count = 0

iteration - N times
because we dont know how many numbers there are we can say that 
iteration will happen N times N being the number of numbers in the file

grants - N * 2 times
every iteration the algorithm grans 2 values a new value 
1.it adds a numbers to the sum variable
2.it adds 1 to the count variable
so every iteration it gratnts 2 * N times

division - 1 times
'''