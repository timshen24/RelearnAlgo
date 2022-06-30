# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         insert_val = arr[i]
#         j = i - 1
#         while j >= 0 and insert_val < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = insert_val

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_val = arr[i]
        j = i
        while j - 1 >= 0 and arr[j - 1] > arr[j]:
            arr[j] = arr[j - i]
            j -= 1
        arr[j] = insert_val
        if i ==2:
            break

if __name__ == '__main__':
    arr = [12, 1, 3, 45, 6, 0, -3, 12, 35, 16]
    insertion_sort(arr)
    print(arr)
