class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class child(person):
    pass
p1 = child("John",36)



print(p1.name)
print(p1.age)