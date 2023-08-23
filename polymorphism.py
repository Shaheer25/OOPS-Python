class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def animal_sound(animal):
    return animal.speak()

dog=Dog()
cat=Cat()


print(animal_sound(dog))
print(animal_sound(cat))