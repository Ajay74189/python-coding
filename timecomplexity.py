a=[12,4,55,6]
print(a[3])
#o(n)
n=5
for i in range(n):
    print(i,end=" ")
#o(n^2)
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()