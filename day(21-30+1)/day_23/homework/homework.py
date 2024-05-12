#create a function called find last even
def find_last_even(numbers_list):
    #create a for loop and iterate over the list 
    #i becomes last numbers index and every iteration -1
    for i in range(len(numbers_list) - 1, -1, -1):
        #check if i is even
        if numbers_list[i] % 2 == 0:
            #if i is even return the number that on the i index of the list
            return numbers_list[i]

print(find_last_even([1,2,3,4,5]))