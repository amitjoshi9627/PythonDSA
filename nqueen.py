
'''
N Queen Problem. 

Printing all possible Solutions to N Queen Problem.

'''

import numpy as np


def pr(arr):
    print('[', end='')
    print(*[np.argmax(i)+1 for i in arr], end='')
    print(']', end=' ')


def is_vaild(arr, r, c):

    for i in range(r):
        if arr[i][c] == 1:
            return False

    for j in range(c):
        if arr[r][j] == 1:
            return False

    i, j = r, c
    while i > -1 and j > -1:

        if arr[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = r, c
    while i < n and j > -1:
        if arr[i][j]:
            return False
        i += 1
        j -= 1
    return True


def solve(arr, r, c):
    if c >= n:
        pr(arr)
        return
    for i in range(0, n):
        if is_vaild(arr, i, c):
            arr[i][c] = 1
            solve(arr, r, c+1)
            arr[i][c] = 0


n = int(input())
mat = [[0 for i in range(n)] for _ in range(n)]

solve(mat, 0, 0)
print()
