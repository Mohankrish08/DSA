def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and key < lst[j]:
            lst[j+1]  = lst[j]
            j -= 1 
        lst[j+1] = key
    return lst

lst = [10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(lst))