
def digital_root(n):
    s = 0
    for i in str(n):
        s = s + int(i)
        l = str(s)
    if(len(l)>1):  
        return digital_root(l)
    else:
        return l
n = input("enter the digit")
print(digital_root(n))


