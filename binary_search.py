def binary_search(arr, target):
    l, r = 0, len(arr)
    while l<r:
        mid = int((l+r)/2)
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid+1
        else:
            r = mid
    return -1


if __name__ == '__main__':
    data = [i for i in range(100000)]
    # print(data)
    for n in data:
        print(binary_search(data, n))
