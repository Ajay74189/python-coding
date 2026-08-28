try:
    print(a)
except NameError:
    print("Error:the variable is doesn't exist")
finally:
    print("it is a finally blockk")
