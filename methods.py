#Types of Methods
#instance->Acessors and Mutators,
# class,
# static

class Students:

    school ="BIT"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def getters(self): #Aceesors
        return self.m1

    def setters(self,other): #mutators
        return self.m1==other

    @classmethod #Decorators which is optional in python 3.11
    def getSchool(cls): #class Methods we use cls intead of self
        return cls.school

    @staticmethod
    def info():
        print("This is Static method which is used when we dont want any relationship in class or obj")


ravi= Students(99,98,99)
raju = Students(35,68,54)

print(ravi.average())

print(ravi.getSchool())

Students.info()