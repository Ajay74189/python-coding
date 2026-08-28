try:
    dict={"berry":1,"cherry":2}
    print(dict["kiwi"])
except KeyError:
    print("the key is doesn't exist")
finally:
    print("it is a finally blockk")


