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


class Parent:
    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def child_method(self):
        print("Child method")

child = Child()
child.parent_method()
child.child_method()