
def is_valid(ans, a):
    return tuple(a) not in ans


def solve(arr, ans, c, j):
    for i in range(j, len(arr)):
        if is_valid(ans, arr):
            ans.add(tuple(arr))
            c[0] += 1
        arr[i], arr[j] = arr[j], arr[i]
        solve(arr, ans, c, i+1)
        arr[i], arr[j] = arr[j], arr[i]


s = input()
s = list(s)
c = [0]
ans = set()
solve(s, ans, c, 0)
print(c[0], ans)
