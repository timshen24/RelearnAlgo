w=[1,2,3]
v=[6,10,12]
memo = [[-1 for i in range(5 + 1)] for j in range(len(w))]

def recur(index, c):
    if index < 0 or c < 0:
        return 0
    if memo[index][c] != -1:
        return memo[index][c]
    res = recur(index - 1, c)
    if c - w[index] >= 0:
        res = max(res, v[index] + recur(index - 1, c - w[index]))
    memo[index][c] = res
    return res

n = len(w)
print(recur(n - 1, 5))