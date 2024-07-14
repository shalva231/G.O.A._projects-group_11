def factorial_division(n, d):
    N = 1
    D = 1
    for i in range(n,1,-1):
        N *= i
    for i in range(d,1,-1):
        D *= i
    
    return N // D