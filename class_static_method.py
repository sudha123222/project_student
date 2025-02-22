class Student:
    #class variables
    school_name='ABC School'

    #constructor
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age

    #instance variables
    def show(self):
        print(self.name,self.age,Student.school_name)

    #class method
    @classmethod
    def change_school(cls,name):
        cls.school_name=name
        print(cls.school_name)

    #static method
    @staticmethod
    def find_notes(subject_name):
        print(subject_name)
        
#create Object        
John=Student('John',12)
#call instance method
John.show()
#call class method using the class
Student.change_school('XYZ School')
#call class method using the object
John.change_school('PQR School')
#call static method using the class
Student.find_notes('maths')
#call class method using the object
John.find_notes('math')