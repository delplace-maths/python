import matplotlib.pyplot as plt
plt.axis([-1,7,-2,30])
x=[n for n in range(7)]
y=[n**2-2*n for n in range(7)]
plt.scatter(x,y)
plt.grid()
plt.show()
