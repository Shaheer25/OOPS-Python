class Car:
    wheel=4 #static vars
    def __init__(self):
        self.mileage = "25"#instance vars
        self.brand="Audi"


c1=Car()
c2=Car()

Car.wheel=3 #makes changes in every objects
print(c1.brand,c1.mileage,c1.wheel)
c1.mileage="20"

