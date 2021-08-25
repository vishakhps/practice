
def tr(n):
    n1 = 1
    n2 = 1
    n3 = 1
    c = 0
    if n == 1:
        print(n1)
    else:
        while(c < n ):
            print(n1)
            sum = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = sum
            c +=1
tr(5)

        

            


    