r_p_s = {"Rock","Paper","Sissor"}
n = input("Enter your choice : Rock,paper or sissor")
limit =int(input("enter the number of games you like to play"))
value = "paper"                #r_p_s.pop()
c = 0
w = 0
l = 0
for i in range(0,limit):
    if n == value:
        c += 1
    elif (n == "rock" and value == "Paper") or (n == "Paper" and value == "Sissor") or (n =="Sissor" and value == "Rock"):
        l += 1
        print(value)
    else:
        w += 1
print("Your win is",w)
print("Loss",l)
print("tie",c)


