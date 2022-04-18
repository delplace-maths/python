from math import *
def delta():
  print('a*x**2 + b*x + c = 0')
  a=float(input('a = '))
  b=float(input('b = '))
  c=float(input('c = '))
  delta=b**2-4*a*c
  print('Delta =',delta)
  if delta < 0:
    print('Pas de solution')
  elif delta == 0:
    print('Une solution double :',-b/(2**a))
  else:
    print('Deux solutions : ',(-b-sqrt(delta))/(2*a),' et ',(-b+sqrt(delta))/(2*a))
    
delta()
