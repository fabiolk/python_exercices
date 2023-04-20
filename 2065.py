aux1 = input().split()
n = int(aux1[0])
m = int(aux1[1])
v = input().split()
c = input().split()
aux2 = [0] * n 
for j in range(m):
  i = aux2.index(min(aux2))  
  aux2[i] += int(v[i]) * int(c[j])  

print(max(aux2))