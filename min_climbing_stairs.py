'''

Leetcode Q.746 Minimum Climbing Stairs.

'''


def minCostClimbingStairs(self, cost):
    dp = [float("inf") for i in range(len(cost)+1)]
    dp[0], dp[1] = 0, 0

    for i in range(2, len(dp)):
        dp[i] = min(dp[i], dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[-1]


if __name__ == "__main__":
    cost = [int(i) for i in input().split()]

    print(minCostClimbingStairs(cost))
