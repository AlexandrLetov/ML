# import csv
# from collections import Counter

# X = []
# Y = []
# with open('./Data/11.csv') as f:
#     reader = csv.DictReader(f, delimiter=';')
#     for row in reader:
#         temp = row['X1']
#         temp2 = row['Y1']
#         X.append(temp)
#         Y.append(temp2)

# print(X)
# print(Y)

from pandas import read_csv, DataFrame
import numpy as np
import matplotlib

dataset = read_csv('./Data/11.csv', delimiter=';')
print(dataset.head())

print(np.mean(dataset['X1']))
