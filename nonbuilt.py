n=int(input("enter size of the list:"))
a=[]
for i in range(n):
    i=int(input())
    a.append(i)
large=a[0]
for i in a:
    if i>large:
        large=i
    print(large)
    