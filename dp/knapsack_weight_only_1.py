# Input
# weights: A list of items and their weights.
weights = [1, 3, 3, 5]
# Output
# A list of possible sums using the weights.
# Output: [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12]

n = len(weights)
max_weights = max(weights)
nums = set()


def carry_or_not(index: int, curWeightSum):
    if index == n:
        nums.add(curWeightSum)
        return
    carry_or_not(index + 1, curWeightSum)
    carry_or_not(index + 1, curWeightSum + weights[index])


carry_or_not(0, 0)
print(list(nums))