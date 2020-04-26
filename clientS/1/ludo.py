import numpy as np

data = np.genfromtxt('./ludo.csv', delimiter=',', names=True)

print(data)