sum = 0
c = 0
l = int(input("Enter the limit of number"))
while c < l :
    n = int(input("enter the number"))
    if(n % 4 == 0):
        sum = sum + n
        c = c + 1
    else:
        print("This number is not divisible by 4 Do  you like to continue")
        choice = input("enter the choice yes or no")
        if(choice == "yes"):
            continue
        else:
            break

print("the sum of number divisible by 4 is ", sum)
