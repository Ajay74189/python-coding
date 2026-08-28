class A:
    def mobile(self):
        print("its displaying the class A")
class B(A):
    def mobile(self):
        print("its displaying the class b")
ob=B()
ob.mobile()