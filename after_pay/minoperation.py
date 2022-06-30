import math
from typing import List


def minOperation(arr: List[int]) -> int:
    i = 1
    maxDistance = -1
    curDistance = 0
    while i <= len(arr) - 1:
        if arr[i] <= arr[i - 1]:
            curDistance += arr[i - 1] - arr[i]
        else:
            maxDistance = max(maxDistance, curDistance)
            curDistance = 0
        i += 1
    res = 0
    while maxDistance > 0:
        maxDistance -= math.pow(2, res)
        res += 1
    return res + 1


print(minOperation([1, 2, 100, 99, 0, 30, 50, 200, 190, 180, 170, 150, 100, 20, 0]))