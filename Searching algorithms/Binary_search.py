def binary_search(arr, value):
    start = 0
    end = len(arr) - 1
    middle = (start+end)//2
    while not (arr[middle]==value) and start <= end:
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        
        middle = (start+end)//2

    if arr[middle] == value:
        return middle
    else:
        return -1
    
arr = [10,20,30,40,50,60,70,80,90]
print(binary_search(arr, 80))