def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return -1


if __name__ == '__main__':
    data = [-1,0,3,5,9,12]
    # print(data)
    for n in data:
        print(binary_search(data, 2))
