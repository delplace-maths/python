import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.5, 2, 100)
y = x**2 - x -3
plt.plot(x,y,label="y=x**2-x-3")

plt.xlim(-3, 3)
plt.xticks(np.linspace(-3, 3,7))
plt.yticks(np.linspace(-3, 10,14))
plt.xlabel("axe des abscisses")
plt.ylabel("axe des ordonnées")
plt.grid()
plt.legend(loc='upper center')
plt.title("Une courbe")
plt.show()
