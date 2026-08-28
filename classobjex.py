class Laptop:
    windows_version=11
    def performance(self):
        print("good")
    def storage(self):
        print("high")
hp=Laptop()
hp.performance()
hp.storage()
hp.windows_version=12
print(hp.windows_version)    
hp.performance()
hp.storage()
dell=Laptop()
dell.performance()
dell.storage()
acer=Laptop()
acer.performance()
acer.storage()
