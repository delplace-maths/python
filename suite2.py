#On considère une suite (u_n) définie par :#
#u(0) = 5#
#u(n+1)=2*u(n)+4#
#A partir de quel entier n, u(n)>10**6 ?#
#Que vaut n et u(n)?#

def rang(M):
  n=0
  u=5
  L=[5]
  while u<=10**6:
    n=n+1
    u=2*u+4
    L.append(u)
  return n,L
  
a,L=rang(10**6)
print('A partir de ',a,', u(n) > 10**6')
print('u(',a-1,') = ',L[a-1])
print('u(',a,') = ',L[a])
