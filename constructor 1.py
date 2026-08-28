class Car:
    def __init__(self,no_of_wheels,no_of_airbags,no_of_seats):
        self.no_of_wheels=no_of_wheels
        self.no_of_airbags=no_of_airbags
        self.no_of_seats=no_of_seats
    def milage(self):
        print("good")
    def speed(self):
        print("Better")
TATA=Car(4,5,6)
TATA.speed()
suzuki=Car(4,5,6)
suzuki.milage()

