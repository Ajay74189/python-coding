import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
max=a[0]
for n in a:
    if n>max:
        max=n
print("maximum:",max)