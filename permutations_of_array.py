
def is_valid(arr, a):
    # print(arr, a)

    return len(arr) == len(a)


def solve(arr, ans, a, j):
    for i in range(j, len(arr)):
        ans.add(tuple(arr))
        arr[i], arr[j] = arr[j], arr[i]
        solve(arr, ans, a, j+1)
        arr[i], arr[j] = arr[j], arr[i]


arr = [int(i) for i in input().split()]
ans = set()
solve(arr, ans, [], 0)
ans = list(ans)
print(ans)
