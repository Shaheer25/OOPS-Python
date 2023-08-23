class Grandparents:
    def Property1(self):
        print("This is Grandparent's Property")

class Parents(Grandparents):#single level
    def Property2(self):
        print("This is Parent's Property")

class Child(Parents) : #multi level
    def Property3(self):
        print("This is Child Property")


property=Child()

# property.Property1()
# property.Property2()
property.Property1()
property.Property2()
property.Property3()


#multiple means
# class Child(Grandparents,Parents)
#this is because when Parent doesnt inherit GrandParents