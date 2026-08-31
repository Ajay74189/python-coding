import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
sum=0
for i in a:
    sum+=i
print(sum)
    