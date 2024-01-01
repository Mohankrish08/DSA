def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(6))