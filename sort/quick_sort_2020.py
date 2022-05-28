from random import randint


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     pivot = array[-1]
#     left = [i for i in array[:-1] if i <= pivot]
#     right = [i for i in array[:-1] if i > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    left = [i for i in arr[:-1] if i <= pivot]
    right = [i for i in arr[:-1] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def rand3WaySort(arr):
    if len(arr) < 2:
        return arr
    index = randint(0, len(arr) - 1)
    pivot = arr[index]
    left = [i for i in arr if i < pivot]
    medium = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return rand3WaySort(left) + medium + rand3WaySort(right)

# def partition(arr, startIndex, endIndex):
#     randInd = randint(startIndex, endIndex)
#     arr[startIndex], arr[randInd] = arr[randInd], arr[startIndex]
#     pivot = arr[startIndex]
#     left, right = startIndex, endIndex
#     while left < right:
#         while left < right and arr[right] > pivot:
#             right -= 1
#         while left < right and arr[left] <= pivot:
#             left += 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#     arr[startIndex], arr[left] = arr[left], arr[startIndex]
#     return left

def partition(arr, l, r):
    pivot = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[l] = arr[l], arr[j]
    return j

def quickSortInPlace(arr, startIndex, endIndex):
    if startIndex > endIndex:
        return
    pivotIndex = partition(arr, startIndex, endIndex)
    quickSortInPlace(arr, startIndex, pivotIndex - 1)
    quickSortInPlace(arr, pivotIndex + 1, endIndex)

def random3WayQuickSort(arr, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    randInd = randint(startIndex, endIndex)
    pivot = arr[randInd]
    lt, eq, gt = startIndex - 1, startIndex, endIndex + 1
    while eq < gt:
        if arr[eq] < pivot:
            lt += 1
            arr[eq], arr[lt] = arr[lt], arr[eq]
            eq += 1
        elif arr[eq] == pivot:
            eq += 1
        elif arr[eq] > pivot:
            gt -= 1
            arr[eq], arr[gt] = arr[gt], arr[eq]
    random3WayQuickSort(arr, startIndex, lt)
    random3WayQuickSort(arr, gt, endIndex)

if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3, 3, 2, 2]))
    print(rand3WaySort([10, 5, 2, 3, 3, 2, 2]))
    arr = [4, 7, 6, 5, 3, 2, 8, 1]
    quickSortInPlace(arr, 0, len(arr) - 1)
    print(arr)
    arr = [4, 9, 4, 3, 1, 9, 4, 3, 9, 4, 9, 1, 4]
    random3WayQuickSort(arr, 0, len(arr) - 1)
    print(arr)
