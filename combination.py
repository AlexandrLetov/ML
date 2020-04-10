from itertools import *
K = 4

matrix = ['*', '-', '+']


for i in product(matrix, repeat=4):
    print(i, end=' ')

#eval метод