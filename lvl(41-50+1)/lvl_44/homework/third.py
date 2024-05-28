def are_all_distinct(a, b, c):
    if a != b:
        if a != c:
            if b != c:
                return True
    return False



'''
All three numbers are distinct:

In this case, the algorithm will perform 3 comparisons 
as it checks to see that they are not the same.
Comparisons:
a != b
a != c
b != c
Total comparisons: 3


Two numbers are the same:

When two numbers are the same, the algorithm could perform
1 comparison 2 comparisons or 3 comparisons 
based on which number is the one thats the same as the other 

if:
a != b (fails)
a != c
b != c
Total comparisons: 1

elif:
a != b 
a != c (fails)
b != c
Total comparisons: 2

elif:
a != b 
a != c 
b != c (fails)
Total comparisons: 3



All three numbers are the same:

when all three numbers are the same, 
the algorithm will perform only 1 operation.
when the algorithm checks and sees that the first operation is False
it will stop and return False


Comparisons:
a != b (fails)
a != c (fails)
b != c (fails)
Total comparisons: 1

'''