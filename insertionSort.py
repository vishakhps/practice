def insertionSort(arr):
    n = int(len(arr))
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)



