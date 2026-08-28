try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError:
    print("error:invalid input")
except ZeroDivisionError:
    print("error:can't divisible by zero")
else:
    print("no error:",a/b)
finally:
    print("exception completed")