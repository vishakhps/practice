def words_to_sentence(words):
    newArr = []
    str1 = " "
    for i in words:
        newArr.append(i) 
    return str1.join(newArr)
list1 = ["bacon","is","delicious"]
print(words_to_sentence(list1))