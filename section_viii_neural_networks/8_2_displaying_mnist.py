import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('../data/mnist_784.csv', delimiter=",", nrows=1)

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

pixels = np.array(X, dtype='uint8')

# Reshape the array into 28 x 28 array (2-dimensional array)
pixels = pixels.reshape((28, 28))

# Plot
plt.title('Label is {label}'.format(label=Y))
plt.imshow(pixels, cmap='Blues')
plt.show()