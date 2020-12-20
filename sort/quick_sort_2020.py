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

# def rand_quicksort(arr): # 这也是三路快排了
#     if len(arr) < 2:
#         return arr
#     index = randint(0, len(arr) - 1)
#     pivot = arr[index]
#     left = [i for i in arr if i < pivot]
#     medium = [i for i in arr if i == pivot]
#     right = [i for i in arr if i > pivot]
#     return quicksort(left) + medium + quicksort(right)

def rand3WayQuickSort(arr):
    if len(arr) < 2:
        return arr
    index = randint(0, len(arr) - 1)
    pivot = arr[index]
    left = [i for i in arr if i < pivot]
    medium = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return rand3WayQuickSort(left) + medium + rand3WayQuickSort(right)

if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3, 3, 2, 2]))
    print(rand3WayQuickSort([10, 5, 2, 3, 3, 2, 2]))
