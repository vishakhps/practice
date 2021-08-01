
def encode(str):
    thisList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    outputList = []
    c = 0
    for i in range(0,len(thisList)):
        for j in range(0,len(str)):
            if str[j] == thisList[i]:
                c += 1
                x = str[j] 
            else:
                if c != 0:
                    txt = c,x
                    outputList.append(txt) 
                    c = 0
                    continue 
        
    print("The string is",outputList)

n = ["A","A","A","B","C","C","A","A"]
encode(n)
#output should be 2Ab3C2A


    
