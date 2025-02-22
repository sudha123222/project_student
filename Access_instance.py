#ways to access instance variable
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name:",stud.name,"Age:",stud.age)
    
stud=Student("Jessa",20)
stud.show()
        