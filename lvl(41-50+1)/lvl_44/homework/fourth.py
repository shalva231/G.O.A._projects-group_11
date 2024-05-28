def find_largest(a, b, c):
    if a > b:
        if a > c:
            return a
        elif c > a:
            return c
    elif b > a:
        if b > c:
            return b
        elif c > b:
            return c
        

'''
the integers are all distinct 

there can be 3 possibility
1. a is the largest
2. b is the largest
3. c is the largest


if a is the largest then the algorithm will do
2 comparisons first a > b and the second a > c

if b is the largest then the algorithm will do
3 comparisons first a > b and the second b > a and the last b > c

if c is the largest then the algorithm will do
3 if a is the second largest number
first a > b second a > c and the last c > a

4 if b is the second largest number
first a > b  second b > a  fourth b > c and the last c > b
''' 


'''
the least comarisons happen when a is the largest only 2 comparisons happen this time

the most hapopen when the c is the largest and b is the second largest number 4 comparisons happen this time
'''


