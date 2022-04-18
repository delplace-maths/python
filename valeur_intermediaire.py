import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.00032*x**6-0.01032*x**5+0.11*x**4-0.355*x**3-0.6*x**2+3.5*x+1

x = np.linspace(-3, 10, 1000)
x_A = -2
x_B = 8
y_h = 2
x_0 = 0.304167
x_1 = 3.72212
x_2 = 6.68897

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# repere
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
plt.xticks([], [])
plt.yticks([], [])

plt.plot(x, f(x))

plt.plot(x_A, f(x_A), "rx")
plt.plot([x_A, x_A], [f(x_A), 0], "r--")
plt.plot([x_A, 0], [f(x_A), f(x_A)], "r--")
ax.annotate("A", (x_A, f(x_A)), (x_A-0.5, f(x_A)-0.5), color="red")
ax.annotate(r"$a$", (x_A, 0), (x_A, 0.2))
ax.annotate(r"$f(a)$", (0, f(x_A)), (0.2, f(x_A)))

plt.plot(x_B, f(x_B), "rx")
plt.plot([x_B, x_B], [f(x_B), 0], "r--")
plt.plot([x_B, 0], [f(x_B), f(x_B)], "r--")
ax.annotate("B", (x_B, f(x_B)), (x_B+0.2, f(x_B)), color="red")
ax.annotate(r"$b$", (x_B, 0), (x_B, -0.6))
ax.annotate(r"$f(b)$", (0, f(x_B)), (-0.8, f(x_B)))

plt.axhline(y=y_h, color="green")
ax.annotate(r"$h$", (0, y_h), (-0.5, y_h+0.2))

plt.plot(x_0, f(x_0), "mx")
plt.arrow(x_0, f(x_0), 0, -f(x_0),  head_width=0.2, head_length=0.3, length_includes_head=True, color="purple", linestyle=(5, (3,3)))
ax.annotate(r"$x_0$", (x_0, 0), (x_0, -0.6), color="magenta")

plt.plot(x_1, f(x_1), "mx")
plt.arrow(x_1, f(x_1), 0, -f(x_1),  head_width=0.2, head_length=0.3, length_includes_head=True, color="purple", linestyle=(5, (3,3)))
ax.annotate(r"$x_1$", (x_1, 0), (x_1, -0.6), color="magenta")

plt.plot(x_2, f(x_2), "mx")
plt.arrow(x_2, f(x_2), 0, -f(x_2),  head_width=0.2, head_length=0.3, length_includes_head=True, color="purple", linestyle=(5, (3,3)))
ax.annotate(r"$x_2$", (x_2, 0), (x_2, -0.6), color="magenta")

plt.show()
