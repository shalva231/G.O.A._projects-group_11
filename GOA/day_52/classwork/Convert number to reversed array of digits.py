def digitize(n):
    n_str = str(n)[::-1] 
    list = [] 
    
    for i in n_str:
        list.append(int(i))

    return list