from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('./assets/data.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

# Getting the values and plotting it
f1 = data['X1'].values
f2 = data['X2'].values
X = np.array(list(zip(f1, f2)))
k=3


# Euclidean Distance Caculator
def dist(a, b, ax, n):
    return np.linalg.norm(a - b, axis=ax, ord=n)

# def dist_min(a,b,)


# def k_means(k,p_choice):
# random centroids
C_x = np.random.randint(0, np.max(X)-20, size=k)
C_y = np.random.randint(0, np.max(X)-20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(C)

# plt.figure(1)
# Plotting along with the Centroids
plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='g')


plt.figure(1)
# To store the value of centroids when it updates
C_old = np.zeros(C.shape)
# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))
# Error func. - Distance between new centroids and old centroids
error = dist(C, C_old, None,2)
# Loop will run till the error becomes zero
while error != 0:
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = dist(X[i], C,1,2)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    # Storing the old centroid values
    C_old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None,2)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
plt.show()


# if __name__ == "__main__":
#     # Importing the dataset
#     data = pd.read_csv('./assets/data.csv')
#     print("Input Data and Shape")
#     print(data.shape)
#     data.head()

#     # Getting the values and plotting it
#     f1 = data['X1'].values
#     f2 = data['X2'].values
#     X = np.array(list(zip(f1, f2)))

#     #plot_points(data_points)
#     p_choice = 0
#     print("PROXIMITY MEASURES:\n\n1. Euclidean Distance\n2. Minkowski Distance\n3. Pearson Correlation \n4. Spearman Correlation")
#     while p_choice not in [1, 2, 3]:
#         p_choice = int(input("Choose proximity measure to be used: "))
#     if(p_choice == 1):
#         p_measure = 'e'
#     elif(p_choice == 2):
#         p_measure = 'm'
#     elif(p_choice == 3):
#         p_measure = 'p'
#     elif(p_choice == 4):
#         p_measure = 's'
#     k = int(input("No. of clusters: "))
    
#     k & p_choice