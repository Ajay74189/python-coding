class Bus:
    def __init__(self,no_of_wheels,no_of_doors,no_of_seats):
        self.no_of_wheels=no_of_wheels
        self.no_of_doors=no_of_doors
        self.no_of_seats=no_of_seats       
    def milage(self):
        print("better condition")
    def speed(self):
        print("120KM")
ASHOKLEYLAND=Bus(6,2,30)
ASHOKLEYLAND.speed()
print(ASHOKLEYLAND.no_of_wheels,ASHOKLEYLAND.no_of_doors,ASHOKLEYLAND.no_of_seats)
bharathbenz=Bus(4,2,20)
bharathbenz.milage()
print(bharathbenz.no_of_wheels,bharathbenz.no_of_doors,bharathbenz.no_of_seats)


