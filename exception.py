try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Error:can't divisible by zero")
finally:
    print("Exception completed")