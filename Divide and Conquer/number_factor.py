def numFactor(n):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numFactor(n-1)
        subP2 = numFactor(n-3)
        subP3 = numFactor(n-4)
        return subP1+subP2+subP3
    
print(numFactor(5))