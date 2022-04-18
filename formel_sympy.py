from sympy import symbols, ln, diff, exp, integrate, expand, factor, solve, lambdify, Eq

x = symbols('x')
f = (2*x+3)*exp(-x)
f1 = diff(f,x)#f'
f2 = diff(f1,x)#f''
f3 = diff(f2,x)#f'''
print("f(x) =",f)
r = 5
print("f(",r,") =",f.subs(x,r))#calcul d'image
print("f'(x) =",f1)
f1_bis = factor(f1)#dérivée factorisée
print("f'(x) =",f1_bis)
z = solve(Eq(f1,0))
print("f'(x) = 0 pour x =",z)
if z != False:
  for i in range(len(z)):
    print("f(",z[i],") =",f.subs(x,z[i]))
F = integrate(f,x)#primitive
print("F(x) =",F)
a,b=0,2
print(u"\u222B(", f, ",(x ,",a,",",b,")) = ",integrate(f,(x,a,b)))
c=3
print("Tangente en",c,": y =",expand(f1.subs(x,c)*(x-c)+f.subs(x,c)))
dl3 = f.subs(x,0)+f1.subs(x,0)*x+f2.subs(x,0)*x**2/2+f3.subs(x,0)*x**3/6
print("DL3(0)=",dl3)
