'''

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.

'''


def coinChange(coins, amount):

    if amount == 0:
        return 0

    mat = [float("inf") for i in range(amount)]

    for i, j in enumerate(coins):
        if j - 1 < len(mat):
            mat[j-1] = 1
    for i, j in enumerate(mat):
        for k in coins:
            if i - k >= 0:
                mat[i] = min(mat[i], mat[i-k]+1)

    return mat[amount - 1] if mat[amount - 1] != float("inf") else -1


if __name__ == "__main__":

    coins = [int(i) for i in input().split()]
    amt = int(input())

    print(coinChange(coins, amt))
