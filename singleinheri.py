class mobile:
    def ringtone(self):
        print("ringing")
    def camera(self):
        print("photo")
class vivo(mobile):
    def storage(self):
        print("storage is high")
ob=vivo()
ob.ringtone()
ob.camera()
ob.storage()