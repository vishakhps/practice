
def vowels(s1):
    thisList = ["a","e","i","o","u"]
    c = 0
    for i in s1:
        for j in thisList:
            if i == j:
                c += 1
    print("this string contains  vowels" , c)
def consonants(s1):
    thisList = ["b","c","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    c1 = 0
    for i in s1:
        for j in thisList:
            if i == j:
                c1 += 1
    print("this string contains consonants " , c1)

s1 = "vishakh"
vowels(s1)
consonants(s1)
