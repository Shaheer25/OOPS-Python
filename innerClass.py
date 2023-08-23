class Students:

    def __init__(self,skill,usn):
        self.skill= skill
        self.usn= usn
        self.laptop=self.Laptop()

    def show(self):
        print(self.usn,self.skill)
        self.laptop.show()
    class Laptop:

        def __init__(self):
            self.brand="HP"
            self.cpu="i5"

        def show(self):
            print(self.cpu,self.brand)


ravi =Students("python","25")
raju = Students("C++","17")

print(id(ravi.laptop))
ravi.show()