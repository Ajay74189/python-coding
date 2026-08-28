class A:
    def __init__(self):
        print("Hii")
class B(A):
    def __init__(self):
        print("Hello")
        super().__init__()
ob=B()