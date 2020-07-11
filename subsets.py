'''

Given an array of integers that might contain duplicates, return all possible subsets.

'''


def pr(arr):
    print('[', end='')
    print(*arr, end='')
    print(']', end=' ')


def is_valid(a, ans):

    return tuple(a) not in ans


def solve(arr, ans, j, a):
    if len(arr) == j:
        if is_valid(a, ans):
            ans.add(tuple(a))
            pr(a)
        return
    for i in range(j, len(arr)):
        a += [arr[i]]

        if is_valid(a, ans):
            pr(a)
            ans.add(tuple(a))

            solve(arr, ans, i+1, a)
            a.pop()
        else:
            a.pop()


arr = [int(i) for i in input().split()]
ans = set()
ans.add(tuple())
pr([])
solve(arr, ans, 0, [])
print()
