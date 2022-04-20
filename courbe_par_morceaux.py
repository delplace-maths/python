# https://trinket.io/python3/1f1aff39df
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.5, 2, 100)
y = x**2 - x -3
plt.plot(x,y,c='b')

x = np.linspace(2, 5, 100)
y = x + 1
plt.plot(x,y,c='b')

x = 2
y = -1
plt.scatter(x,y,c='b')

plt.xlim(-3, 3)
plt.xticks(np.linspace(-3, 6,10))
plt.yticks(np.linspace(-3, 8,12))
plt.grid()
plt.show()
