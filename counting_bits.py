'''

Counting Number of set bits for every numbers i in the range 0 ≤ i ≤ num.

'''


def countBits(num):

    if num == 0:
        return [0]
    dp = [0] * (num+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(dp)):
        x = 2 ** int(math.log(i, 2))
        dp[i] = dp[i - x] + 1
    return dp


if __name__ == '__main__':

    num = int(input())
    print(countBits(num))
