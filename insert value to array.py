import array
arr=array.array('i',[1,3,4,78,7])
arr.insert(3,5)
print(arr)
#deleteinarray
arr.remove(78)
print(arr)
#removebyindex
arr.pop(1)
print(arr)
#removelastindex
arr.pop()
print(arr)
#count apprends of an element
b=array.array('i',[10,20,20,40,20])
count=b.count(20)
print(count)
#average array common methods
c=array.array('i',[1,2,3,4,10])
avg=sum(c)//len(c)
print(avg)




