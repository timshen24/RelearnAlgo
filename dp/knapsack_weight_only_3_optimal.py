# Input
# weights: A list of items and their weights.
weights = [1, 3, 3, 5]
# weights = [7, 49, 73, 58, 30, 72, 44, 78, 23, 9, 40, 65, 92, 42, 87, 3, 27, 29, 40, 12]

# Output
# A list of possible sums using the weights.
# Output: [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12]

n = len(weights)
max_weights = sum(weights)

dp = [[False] * (max_weights + 1) for _ in range(2)]


def weight_only():
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(max_weights + 1):
            dp[1][j] = dp[1][j] | dp[0][j]
            if j >= weights[i-1]:
                dp[1][j] = dp[1][j] | dp[0][j-weights[i-1]]
        dp[0] = dp[1]


weight_only()
print(dp)
print(dp[-1])
print([i for i, num in enumerate(dp[-1]) if num])