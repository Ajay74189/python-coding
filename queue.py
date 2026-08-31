from inspect import stack


queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue[0])
print(queue.pop(0))
print(queue)
#reverse queue
l="ajay"
queue=list(l)
result=""
while queue:
    result+=queue.pop()
print(result)