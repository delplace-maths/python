# https://trinket.io/python3/fba4f97d8e
from math import sqrt

def premier(n):
# p est premier si, et seulement si, p n'est pas divisible par k pour tout k compris entre 1 et racine(p)

    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        borne = int(sqrt(n))

        for k in range(3, borne+1, 2):
            if n%k==0:
                return False
        return True


def wilson(n):
# théorème de Wilson: p est premier si, et suelement si, (p-1)! = p-1 mod-p)

    if n==2:
        return True   
    elif n%2==0:
        return False
    else:
        produit=1
        for k in range(2,n):
            produit = (produit*k)%n
        return produit == n-1
        
for i in range(2,500):
  if premier(i):
    print( i , end =" ")
    
print("****************************************************************************************")
    
for i in range(2,500):
  if wilson(i):
    print( i , end =" ")
