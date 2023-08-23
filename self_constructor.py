class Person:

    def __init__(self):
        self.name="shaheer"
        self.age =10

    def update(self):
        self.name="Shahid"

    def compare(self,var):
        if self.age == var.age:
            return True
        else :
            return False


c1= Person()
c2= Person()

if c1.compare(c2):
    print(c1.age , "is same as " , c2.age)
else :
    print("They're Different")

c1.update() #Changes from Shaheer to Shahid

print(c1.name)