# Input
# weights: A list of items and their weights.
# weights = [1, 3, 3, 5]
weights = [7, 49, 73, 58, 30, 72, 44, 78, 23, 9, 40, 65, 92, 42, 87, 3, 27, 29, 40, 12]

# Output
# A list of possible sums using the weights.
# Output: [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12]

n = len(weights)
max_weights = sum(weights)
nums = set()

memo = [[False] * (max_weights + 1) for _ in range(n + 1)]


def carry_or_not(index: int, curWeightSum):
    if index == n:
        nums.add(curWeightSum)
        return
    if memo[index][curWeightSum]:
        return
    memo[index][curWeightSum] = True
    carry_or_not(index + 1, curWeightSum)
    carry_or_not(index + 1, curWeightSum + weights[index])


carry_or_not(0, 0)
print(list(nums))