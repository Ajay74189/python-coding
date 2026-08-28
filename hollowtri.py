n=5
for i in range(n+1):
    for j in range(i):
        if j==0  or i==n or i-1==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
       