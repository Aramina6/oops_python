class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

my_animal = Animal()
my_animal.speak()  # Output: The animal makes a sound.

my_dog = Dog()
my_dog.speak()  # Output: The dog barks.

