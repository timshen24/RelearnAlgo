def merge_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    # the divide step: split array into two components, assuming they are sorted recursively
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # the merging (conquer) step: combine two components to get the final result
    l, r, result = 0, 0, []
    while l < len(left) or r < len(right):
        if l >= len(left) or (r < len(right) and left[l] > right[r]):
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    return result

print(merge_sort([10, 9, 8, 7, 5, 2, 3, 1, 6, 11]))