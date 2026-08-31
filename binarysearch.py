import array
n=int(input())
a=array.array('i')
for i in range(n):
    val=int(input())
    a.append(val)
target=int(input("enter your target value:"))
left=0
right=n-1
result=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        result=mid
        break
    elif a[mid]<target:
        left=mid+1
    elif a[mid]>target:
        right=mid-1
if result!=-1:
    print("element found at index:",result)
else:
    print("element no found")
