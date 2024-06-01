def count_capital(text):
    count = 0
    for i in text:
        if i.isupper():
            count += 1
    return count

print(count_capital("HelLloOw"))

'''
for every letter in the text
    check if the letter is uppercase
        if it is, add 1 to the count
        if its not do nothing and start the cycle from the start.
    return the count
'''

'''
this programm does N comparison it checks
if the letters in the text are uppercase
so the unswer deppends on the number of characters in the text(N)






N=number of characters
   n=number of uppercase characters
if N=4 then n could equal to 4,3,2,1 or even 0
if n=0 the number of increments would equal to 0 because the count variable will not change.
if n=1 the number of increments would equal to 1 because the count variable will only change 1 time.
if n=2 the number of increments would equal to 2 because the count variable wull only change 2 times
if n=3 the number of increments would equal to 3 because the count variable wull only change 3 times
if n=4 the number of increments would equal to 4 because the count variable wull only change 4 times

so the number of increments depents on the number of uppercase characters


the minimum increments that could happen is 0

and the maximum is N the lenght of the text

'''