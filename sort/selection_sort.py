# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_ind = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_ind]:
#                 min_ind = j
#         arr[min_ind], arr[i] = arr[i], arr[min_ind]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]

if __name__ == '__main__':
    l = [3, 4, 2, 1, 5, 6, 7, 8, 30, 50, 1, 33, 24, 5, -4, 7, 0]
    selection_sort(l)
    print(l)
