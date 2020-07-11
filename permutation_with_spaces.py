'''

Given a string you need to print all possible strings
that can be made by placing spaces (zero or one) in between them.

'''


def pr(s):
    s = s.strip()
    print('['+s+']', end=' ')


def solve(s, ans, a, j):

    if len(a) >= 1 and s[-1] == a.replace(' ', '')[-1]:
        pr(a)
        return

    for i in range(j, len(s)):

        a += s[i] + ' '
        # print(a[-1])
        solve(s, ans, a, i+1)
        a = a[:-1]


for i in range(int(input())):

    s = input()
    ans = set()
    solve(s, ans, '', 0)
    print()
