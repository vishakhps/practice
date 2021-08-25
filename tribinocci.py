
def tribonacci(signature, n):
    arr = signature
    newArr = []
    for i in signature:
        n1 = arr[0]
        n2 = arr[1]
        n3 = arr[2]
    c = 0
    if n == 1:
        newArr.append(n1)
        print (newArr)
    else:
        while(c < n ):
            newArr.append(n1)
            sum = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = sum
            c +=1
    return(newArr)
tribonacci([1, 1, 1],10)

