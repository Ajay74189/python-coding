def nested(n):
    if n>100:
        return n-10
    return nested(nested(n+11))
print(nested(95))