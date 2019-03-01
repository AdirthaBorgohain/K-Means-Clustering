import os
import random
import numpy as np
import matplotlib.pyplot as plt


def plot_points(data_points):
    x, y = data_points.T
    plt.scatter(x, y)
    plt.title("Unclustered Data")
    plt.show


def create_centers(k):
    centers = []
    for i in range(k):
        centers.append([random.randint(0, 100), random.randint(0, 100)])
    return np.array(centers)


def k_means(data_points, centers, p_measure):
    label = []
    cluster = []
    total_points = len(data_points)
    k = len(centers)

    for epoch in range(0, 200):
        for index_point in range(0, total_points):
            distance = {}
            for center_index in range(0, k):
                if(p_measure == 'm'):
                    distance[center_index] = minkowski_distance(
                        data_points[index_point], centers[center_index])
                elif(p_measure == 'p'):
                    distance[center_index] = pearson_correlation(
                        data_points[index_point], centers[center_index])
                elif(p_measure == 's'):
                    distance[center_index] = spearman_correlation(
                        data_points[index_point], centers[center_index])
            label = assign_cluster(distance, data_points[index_point], centers)
            centers[label[0]] = compute_new_centers(
                label[1], centers[label[0]])
            if epoch == (200 - 1):
                cluster.append(label)
        return [cluster, centers]


if __name__ == "__main__":
    data_points = np.genfromtxt("assets/data.csv", delimiter=",")
    plot_points(data_points)
    p_choice = 0
    print("PROXIMITY MEASURES:\n\n1. Minkowski Distance\n2. Pearson Correlation \n3. Spearman Correlation")
    while p_choice not in [1, 2, 3]:
        p_choice = int(input("Choose proximity measure to be used: "))
    if(p_choice == 1):
        p_measure = 'm'
    elif(p_choice == 2):
        p_measure = 'p'
    elif(p_choice == 3):
        p_measure = 's'
    k = int(input("No. of clusters: "))
    centers = create_centers(k)
    [cluster, new_centers] = k_means(data_points, centers, p_measure)
