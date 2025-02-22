#modify values of instance variable
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
stud=Student("Jessa",20)
print("Before")
print("Name:",stud.name,"Age:",stud.age)
stud.name="Dhivya"
stud.age=15
print("After")
print("Name:",stud.name,"Age;",stud.age)        