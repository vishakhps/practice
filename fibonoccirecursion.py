def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
n = int(input("Enter the limit"))
print("fibonocci series")
for i in range(0,n):
    print(fib(i))

