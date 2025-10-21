import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

fig.colorbar(cax)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        ax.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', color='w')

plt.show()