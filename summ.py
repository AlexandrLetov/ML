from itertools import *

K = 2
S = 20

matrix = ['ужастик', 'комедия', 'триллер', 'документалка', 'детектив']


for i in combinations(matrix, K):
    # print(i)
    # if sum(i) == S:
    print(i, end=' ')
