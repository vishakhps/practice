def fib(n):
    s1 = 0
    s2 = 1
    sum = 0
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for i in range(1,n):
            sum = sum + i
            s1 = sum
            print (s1)
            s2 = s1
fib(5)


    

    