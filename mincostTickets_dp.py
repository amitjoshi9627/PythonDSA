'''

LeetCode Question.983 (Dynamic Programming): Minimum Cost For Tickets

'''


def mincostTickets(days, costs):

    dp = [float("inf") for i in range(days[-1]+1)]
    dp[0] = 0
    n = len(dp)
    x, y, z = costs
    prev = 0

    for i in range(1, len(dp)):
        if i not in days:
            dp[i] = prev
        else:
            prev = i

    for i in range(1, len(dp)):
        if dp[i] == float("inf"):
            dp[i] = min(dp[i], dp[i-1] + x)
            if i-7 > 0:
                dp[i] = min(dp[i-7]+y, dp[i])
            else:
                dp[i] = min(dp[i], y)
            if i-30 > 0:
                dp[i] = min(dp[i], dp[i-30] + z)
            else:
                dp[i] = min(dp[i], z)
        else:
            dp[i] = dp[dp[i]]

    return dp[n-1]


if __name__ == "__main__":

    days = [int(i) for i in input().split()]
    costs = [int(i) for i in input().split()]

    print(mincostTickets(days, costs))
