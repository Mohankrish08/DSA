def merge(clist, l, m, r):
    n1 = m - l + 1
    n2 = r - m 

    L = [0] * n1 
    R = [0] * n2 

    for i in range(0, n1):
        L[i] = clist[l+ i]

    for j in range(0, n2):
       R[j] = clist[m + 1 + j]

    i = 0
    j = 0
    k = l 

    while i<n1 and j <n2:
        if L[i] <= R[j]:
            clist[k] = L[i]
            i += 1 
        else:
            clist[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        clist[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        clist[k] = R[j]
        j += 1
        k += 1

def mergeSort(clist, l, r):
    if l < r:
        m = (l + r)//2
        mergeSort(clist, l, m)
        mergeSort(clist, m+1, r)
        merge(clist, l, m, r)

lst = [10,9,8,7,6,5,4,3,2,1]
mergeSort(lst, 0, len(lst) - 1)
print(lst)