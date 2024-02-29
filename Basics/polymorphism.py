class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle  speed is 150')


class Car(Vehicle):
    def max_speed(self):
        print('Car  speed is 240')


car = Car('Ford', 'Red', 20000)
car.show()
car.max_speed()

vehicle = Vehicle('Truck200', 'white', 75000)
vehicle.show()
vehicle.max_speed()
