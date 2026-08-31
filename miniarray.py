import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
min=a[0]
for n in a:
    if n<min:
        min=n
print("minimum:",min)