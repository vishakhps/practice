def bubbleSort(arr):
    n = int(len(arr))
    for i in range(0,n):
        for j in range(0,n-i-1):
           if arr[j] > arr[j+1] :
               arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Sorted array:")
    for i in range(0,n):
        print("",arr[i])
arr = [13, 16, 1, 3, 56, 6]
bubbleSort(arr)