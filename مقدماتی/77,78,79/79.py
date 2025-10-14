class Car:
    cars_number=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.status=False
        Car.cars_number+=1

    def start(self):
        if self.status==False:
            self.status=True
            print(f'{self.name} is starting')
        else:
            print(f'baba man is on dont start please')

    def off(self):
        if self.status:
            self.status=False
            print(f'{self.name} is off now')
        else:
            print(f'car is off please start first')

car1=Car('BENZ','1200')
car2=Car('pejo','1500')
print(Car.cars_number)
car3=Car('bmw','1900')
print(Car.cars_number)
# car1.start()
# car1.off()
car3.cars_number=5

Car.cars_number=9

print(Car.cars_number)
print(car1.cars_number)
print(car2.cars_number)

print(car3.cars_number)