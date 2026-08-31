stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])
print(stack.pop())
print(stack)
#reverse stack
l="hello"
stack=list(l)
result=""
while stack:
    result+=stack.pop()
print(result)
#implemenet stack using in queue
import queue
st=queue.LifoQueue()
st.put(10)
st.put(20)
st.put(30)
print(st.get())
print(st.queue)
