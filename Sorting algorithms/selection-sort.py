def selection_sort(clist):
    for i in range(len(clist)):
        min_index = i 
        for j in range(i+1, len(clist)):
            if clist[min_index] > clist[j]:
                min_index = j 
        clist[i], clist[min_index] = clist[min_index], clist[i]
    return clist

lst = [10,9,8,7,6,5,4,3,2,1]
print(selection_sort(lst))