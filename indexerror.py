try:
    a=[1,2,3,4]
    print(a[6])
except IndexError:
    print("error:cant find this index")
else:
    print("no error",a[2])
finally:
    print("exception completed")