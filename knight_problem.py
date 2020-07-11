'''

How many ways are there to place a black and a white knight on an N * M chessboard
such that they do not attack each other?

'''


def is_valid(x1, y1, x2, y2):
	if x1 == x2 and y1 == y2:
		return False
    if x1 + 2 == x2 and y1 + 1 == y2:
        return False
    if x1 + 1 == x2 and y1 + 2 == y2:
        return False
    if x1 - 1 == x2 and y1 - 2 == y2:
        return False
    if x1 - 2 == x2 and y1 - 1 == y2:
        return False

    return True


def solve(n,m, x, y, i, j,coun):



	for x1 in range(n):
		if is_valid(x1,y,i,j):
			coun[0] += 1

			
n,m = map(int,input().split())
coun = [0]
solve(n, x, y, i, j,coun)
