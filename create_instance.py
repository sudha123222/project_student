class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.age)
s1=student("Jessa",20)
print('Object 1')
print("Name:",s1.name)
print("Age:",s1.age)
s2=student("Kelly",10)
print("Object 2")
print("Name:",s2.name)
print("Age:",s2.age)
