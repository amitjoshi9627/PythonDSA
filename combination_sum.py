'''

Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B.
The same repeated number may be chosen from A unlimited number of times.

'''


def pr(ans, check):
    check[0] = True
    print('[', end='')
    print(*ans, end='')
    print(']', end='')


def is_valid(s, k):
    return s < k


def solve(arr, k, ans, s, j, check):
    # print(ans, s)
    if s == k:
        pr(ans, check)
        return
    for i in range(j, len(arr)):
        if is_valid(s, k):
            s += arr[i]
            ans += [arr[i]]
            solve(arr, k, ans, s, j, check)
            ans.pop()
            s -= arr[i]
            j += 1


for i in range(int(input())):
    check = [False]
    n = int(input())
    arr = set([int(i) for i in input().split()])
    k = int(input())
    arr = sorted(arr)
    solve(arr, k, [], 0, 0, check)
    if not check[0]:
        print('No Solution	')
    else:
        print()
