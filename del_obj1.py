#Delete Object 
class persion:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is " + self.name)
p1= persion("john",36)
del p1
print(p1)     