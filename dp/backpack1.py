w=[1,2,3]
v=[6,10,12]

def recur(index, c):
    if index < 0 or c < 0:
        return 0
    res = recur(index - 1, c)
    if c - w[index] >= 0:
        res = max(res, v[index] + recur(index - 1, c - w[index]))
    return res

n = len(w)
print(recur(n - 1, 5))