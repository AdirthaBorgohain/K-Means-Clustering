import os
import random
import numpy as np

def create_centers(k):
    centers = []
    for i in range(k):
        centers.append([random.randint(0,100),random.randint(0,100)])
    return np.array(centers)
        
if __name__ == "__main__":
    data_points = np.genfromtxt("assets/data.csv", delimiter=",")
    p_choice = 0
    print("PROXIMITY MEASURES:\n\n1. Minkowski Distance\n2. \n3. Spearman Correlation")
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
