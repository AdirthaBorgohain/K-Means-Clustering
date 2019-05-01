from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def dist(a, b, ax, n):
    return np.linalg.norm(a - b, axis=ax, ord=n)

data = pd.read_csv('./assets/data.csv')
print("Input Data and Shape")
print(data.shape)

f1 = data['X1'].values
f2 = data['X2'].values
X = np.array(list(zip(f1, f2)))

print("Enter the choice of distance\n")
c = int(input("1. Euclidean \n2. Minkowski\n"))

if c == 1:
    n=2
elif c==2:
    n = int(input("Enter value of n="))
else:
    print("Enter a correct option")
    exit(0)

k = int(input("Enter value of k="))

C_x = np.random.randint(0, np.max(X)-20, size=k)
C_y = np.random.randint(0, np.max(X)-20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)

plt.scatter(f1, f2, c='#050505', s=7)
plt.figure(1)

C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
error = dist(C, C_old, None,2)

while error != 0:
    for i in range(len(X)):
        distances = dist(X[i], C,1,2)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    C_old = deepcopy(C)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None,2)

colors = ['c', 'm','r', 'g', 'b', 'y']
fig, ax = plt.subplots()

for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
plt.show()
