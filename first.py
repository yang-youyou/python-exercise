import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 12 * np.pi, 0.01)
x = np.sin(t) * (np.e ** np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
y = np.cos(t) * (np.e ** np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='yellow', linewidth='3')
plt.hlines(0, -3, 3, color="pink")  # 横线
plt.vlines(0, -2, 3, color="pink")  # 竖线
plt.savefig("as.")
plt.show()
