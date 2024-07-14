def sum_no_duplicates(l):
    sum = 0
    for i in l:
        if not l.count(i) > 1:
            sum += i 
    return sum