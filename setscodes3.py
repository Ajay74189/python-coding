s7="I love python"
s8="I love jave"
print(set(s7.split())^set(s8.split()))
s8={1,2,3}
s9=s8.copy()
s9.add(4)
print(s9)
s10={1,0,9,3}
print(set(sorted(s10)))
s11="hello"
s12="world"
print(set(s11)&set(s12))
s13={1,3,5,6,}
s13.clear()
print(s13)
s14={1,2,3,1,4,5,6,2}
print(s14)
s15=frozenset([1,3,2,4])
print(s15)
a,b,c={1,2},{3,4},{5,6}
print(a.union(b,c))
s16={"apple","orange","berry"}
print("apple" in s16)
s17={1,2,3,4}
s18={2,4,6}
s17.intersection_update(s18)
print(s17)
list=[1,3,3,1,4,5,2,5,6]
print(len(set(list)))
s19={1,2,3}
s20={2,1,3}
print(s19==s20)