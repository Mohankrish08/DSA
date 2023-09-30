def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

arr = [10,20,30,40,50,60,70,80,90]
print(linear_search(arr, 80))