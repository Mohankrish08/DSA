import math 

def insertion_sort(clist):
    for i in range(1, len(clist)):
        key = clist[i]
        j = i-1
        while j>=0 and key < clist[j]:
            clist[j+1] = clist[j]
            j-=1 
        clist[j+1] = key 

    return clist 

def bucket_sort(clist):
    no_of_buckets = round(math.sqrt(len(clist)))
    max_val = max(clist)
    arr = []
    
    for i in range(no_of_buckets):
        arr.append([])
    
    for j in clist:
        index_b = math.ceil(i*no_of_buckets/max_val)
        arr[index_b-1].append(j)

    for i in range(no_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0 
    for i in range(no_of_buckets):
        for j in range(len(arr[i])):
            clist[k] = arr[i][j]
            k += 1 
    return clist

lst = [10,9,8,7,6,5,4,3,2,1]
print(bucket_sort(lst))