d={"a":1,"b":2}
d1={}
print(d)
print(d1)
d2={}
d2["yes"]=1
d2["no"]=2
print(d2)
d3={"red":4,"black":7}
print(d3["red"])
print(d3["black"])
d4={"apple":7,"berry":8,"cherry":9}
print(d4.get("cherry"))
print(d4.get("banana"))
print("apple" in d4)
for value in d4.values():
    print(value)
for key in d4.keys():
    print(key)
for key,value in d4.items():
    print(key,value)
word=("banana")
count={}
for ch in word:
    count[ch]=count.get(ch,0)+2
print(count)
d5={"a":1,"b":2,"c":3,"d":4}
print(sum(d5.values()))
print(d5.values())
print(d5.keys())
d6={"h":-1,"c":4,"z":2}
print(dict(sorted(d6.items())))
d7={"a":28}
d8={"b":9}
d7.update(d8)
print(d7)
keys=["a","b","c"]
values=[1,2,3]
print(dict(zip(keys,values)))
d7={"a":1,"b":2}
d8={"b":2,"a":1}
print(d7==d8)
d9={"b":2,"a":1,"c":-1}
print(min(d9,key=d9.get))
d10={"a":5,"b":4,"c":9}
print(len(d10))
d11={"a":10,"b":5}
d12={"t":10,"b":53}
print(set(d11.keys())&set(d12.keys()))
print(set(d11.values())&set(d12.values()))
d13={"a":1,"b":2}
print(list(d13.items()))
d14=d13.copy()
d14["c"]=9
print(d13,d14)
d15={"a":4,"b":6,"c":4,"e":3}
print(set(d15.values()))