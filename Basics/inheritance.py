class Animal:
    name = "" 
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def display(self):
        print("My name is ", self.name)

d = Dog()

d.name = "Browine"
d.eat()
d.display()
