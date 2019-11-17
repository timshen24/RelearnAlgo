w=[1,2,3]
v=[6,10,12]
c = 5
memo = [0 for i in range(c + 1)]

n = len(w)
for i in range(len(w)):
    for j in range(c, -1, -1):
        memo[j] = max(memo[j], v[i] + memo[j - w[i]] if j >= w[i] else memo[j])

print(memo[-1])