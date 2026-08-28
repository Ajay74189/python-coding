class A:
    def display(self):
        print("its displaying the class A")
class B(A):
    def display(self):
        print("its displaying the class B")
ob=B()
ob.display()