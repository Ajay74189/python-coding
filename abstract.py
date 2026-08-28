class Rice:
    def chickenrice(self):
        pass
    def beefrice(self):
        pass
class whiterice(Rice):
    def chickenrice(self):
        print("chickenrice is junk food")
    def beefrice(self):
        print("beefrice is good for health")
ob=whiterice()
ob.chickenrice()
ob.beefrice()
    