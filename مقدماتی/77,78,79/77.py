class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.status=False

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
car1.start()
# car1.off()
