'''

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

'''


def solve(s, a, ans, j):
    for i in range(j, len(s)):
        if s[i].isdigit():
            a += s[i]
        else:
            a += s[i].upper()
        solve(s, a, ans, i+1)
        x = a[-1]
        a = a[:-1]
        a += x.lower()

    if len(a) >= 1 and a.replace(' ', '')[-1].lower() == s[-1].lower():
        ans.add(a)


s = input()
ans = set()
solve(s, '', ans, 0)
print(list(ans))
