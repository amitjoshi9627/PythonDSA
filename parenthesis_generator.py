'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''


def is_valid(arr, ans):
    if "".join(arr) in ans:
        return False
    stack = []
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return 0
            stack.pop()
    return len(stack) == 0


def not_pair(a1, a2, x1, x2, pair):
    return a1 == ')' and a2 == '(' and pair[x1] != x2


def solve(s, ans, j, n, count1, count2):

    if len(s) > 2*n:
        return
    if len(s) == 2*n and count1 == count2:
        # print(count1, count2)
        ans.add(s)
        return
    i = j

    while i < 2*n:
        # print(s)
        if count1 <= n:
            s += '('
            count1 += 1
            solve(s, ans, i+1, n, count1, count2)
        if count1 - count2 > 0:
            print(count1, count2, s)
            s += ')'
            count2 += 1
        s = s[::-1].replace('(', '', 1)[::-1]
        count1 -= 1

        i += 1


n = int(input())
d = {i: i for i in range(n*2)}
pair = {i: i+1 for i in range(0, n*2, 2)}

for i in range(1, n*2, 2):
    pair[i] = i-1
print(pair)

ans = set()
solve('', ans, 0, n, 0, 0)
print(ans)
