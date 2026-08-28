def even(n):
    if n==0:
        return True
    return odd(n-1)
def odd(n):
    if n==0:
        return True
    return even(n-1)
print(odd(9))