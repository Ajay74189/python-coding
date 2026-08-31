import array
n=int(input())
a=array.array('i')
for i in range(n):
    val=int(input())
    a.append(val)
for i in a:
    print(i,end=" ")