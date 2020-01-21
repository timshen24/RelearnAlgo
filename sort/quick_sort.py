def quick_sort(arr):
    if len(arr) == 0:
        return []
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    a = quick_sort([6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
    print(a)