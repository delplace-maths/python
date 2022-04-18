import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
def f(x):
  return np.exp(x)
xmin = 0
xmax = 2
nb_rectangles = 10
pas = (xmax - xmin)/nb_rectangles
surface_rectangles0 = 0
for i in range(nb_rectangles):
  surface_rectangles0 = surface_rectangles0 + pas * f(xmin+i*pas)
surface_rectangles1 = 0
for i in range(nb_rectangles):
  surface_rectangles1 = surface_rectangles1 + pas * f(xmin+(i+1)*pas)

  
fig, ax = plt.subplots(2,1, figsize=(5, 7.5))

#figure du haut
hidden_line = ax[0].plot([xmin,xmax],[f(xmin),f(xmax)],alpha=0, label=f"Surface des rectangles = {np.round(surface_rectangles0,5)}")

for i in range(nb_rectangles):
  ax[0].add_patch(patches.Rectangle((xmin+i*pas, 0), pas, f(xmin+i*pas), edgecolor = 'blue', facecolor = 'red', fill=True))

L_x = np.linspace(xmin,xmax,100)
L_y = f(L_x)
ax[0].plot(L_x,L_y,c='k')
ax[0].legend(handles=hidden_line)

#figure du bas
hidden_line = ax[1].plot([xmin,xmax],[f(xmin),f(xmax)],alpha=0, label=f"Surface des rectangles = {np.round(surface_rectangles1,5)}")

for i in range(nb_rectangles):
  ax[1].add_patch(patches.Rectangle((xmin+i*pas, 0), pas, f(xmin+(i+1)*pas), edgecolor = 'blue', facecolor = 'red', fill=True))

L_x = np.linspace(xmin,xmax,100)
L_y = f(L_x)
ax[1].plot(L_x,L_y,c='k')
ax[1].legend(handles=hidden_line)

plt.show()
print('Surface sous la courbe :'+str(np.round((surface_rectangles0 + surface_rectangles1)/2,5)))

