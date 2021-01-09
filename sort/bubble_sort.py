# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

nums = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(nums)
print(nums)
