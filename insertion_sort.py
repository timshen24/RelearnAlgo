def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > pivot:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = pivot

arr = [6, 5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > pivot:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = pivot