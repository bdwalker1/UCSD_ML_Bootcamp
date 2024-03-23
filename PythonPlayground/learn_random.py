import random as amoc
import matplotlib.pyplot as plt

def my_random():
    # Random, sale, shift, return
    return amoc.normalvariate(10, 3.5)

hits = []
for i in range(1000000):
    hits.append(my_random())

plt.hist(hits, bins=500)
plt.show()