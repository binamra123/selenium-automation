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