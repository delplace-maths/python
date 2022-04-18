#####pgcd(a,b)=pgcd(b,a-b)#####
def pgcd(a,b):
  if b > a:
    a,b = b,a
  if b == 0:
    return a
  else:
    return pgcd(b,a-b)
#####pgcd(a,b)=pgcd(b,a%b)#####      
def pgcd2(a,b):
  if b == 0:
    return a
  else:
    return pgcd2(b,a%b)
        
print(pgcd(360,240))
print(pgcd2(10236,12336))
