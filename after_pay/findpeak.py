from typing import List


def findPeak(arr: List[int]) -> int:
    l, r = 1, len(arr) - 1
    # boundary_index = -1
    while l <= r:
        mid = (l + r) // 2
        if mid >= 0 and arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid - 1]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(findPeak([1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1]))
