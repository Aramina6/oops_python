class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("The dog barks.")

my_dog = Dog("Buddy")
my_dog.speak()  # Output: The dog barks.
