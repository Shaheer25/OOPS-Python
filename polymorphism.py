class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_sound(animal):
    return animal.speak()

# Creating instances of different classes
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the common function with different objects
print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(cow))
