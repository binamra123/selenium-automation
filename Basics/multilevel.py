class Vehicle:
    def Vehicle_info(self):
        print(' Vehicle class information')

class Car(Vehicle):
    def car_info(self):
        print('Car class information')

class SportsCar(Car):
    def sportscar_info(self):
        print('SportsCar class information')


s_car = SportsCar()

s_car.Vehicle_info()
s_car.car_info()
s_car.sportscar_info()


class Grandparent:
    def __init__(self):
        print("Grandparent class constructor")

    def grandparent_method(self):
        print("Grandparent method")


class Parent(Grandparent):
    def __init__(self):
        super().__init__()  # Call constructor of Grandparent
        print("Parent class constructor")

    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Call constructor of Parent
        print("Child class constructor")

    def child_method(self):
        print("Child method")


grandchild = Child()
grandchild.grandparent_method()
grandchild.parent_method()
grandchild.child_method()
