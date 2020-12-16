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

if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3, 3, 2, 2]))
