#The string representation of an object with the __str__()function
class persion:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name}({self.age})" 
    
p1= persion("john",36)
print(p1)
        