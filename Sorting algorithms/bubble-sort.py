def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [10,9,8,7,6,5,4,3,2,1]
print(bubble_sort(lst))