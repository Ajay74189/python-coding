n=4
adj_matrix=[[0]*n for i in range(n)]
edges=[(0,1),(0,2),(1,2),(2,3)]
for v,e in edges:
    adj_matrix[e][v]=1
    adj_matrix[v][e]=1
for i in adj_matrix:
    print(i)