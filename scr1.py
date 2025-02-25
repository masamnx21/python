import numpy as np

planets = np.genfromtxt('planets.csv', delimiter=',', skip_header=2, encoding='UTF-8', names=True, dtype=None, missing_values='???', filling_values=-10000)


print(planets['diameter'])

