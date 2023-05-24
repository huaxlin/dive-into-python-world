import numpy as np
import matplotlib.pyplot as plt

# Load the data from the text file
data = np.loadtxt('mandelbrot_set.txt')

# Plot the Mandelbrot set
plt.imshow(data.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()

# plt.show()
plt.savefig('mandelbrot_set.png')
