w=[1,2,3]
v=[6,10,12]
c = 5
memo = [[0 for i in range(c + 1)] for j in range(len(w))]
# print(memo[0])
n = len(w)
for i in range(c + 1):
    memo[0][i] = w[0] if i >= w[0] else 0
for i in range(1, len(w)):
    for j in range(c + 1):
        memo[i][j] = memo[i - 1][j]
        if j >= w[i]:
            memo[i][j] = max(memo[i][j], v[i] + memo[i - 1][j - w[i]])

print(memo[len(w) - 1][c])