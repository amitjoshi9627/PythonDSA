
def is_valid(ans, a):
    # print(arr, a)

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
# solve(s[::-1], '', ans, 0, c)
print(c[0], ans)
