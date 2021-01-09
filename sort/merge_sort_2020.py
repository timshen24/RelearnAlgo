def split(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def merge_sorted_arr(list_left, list_right):
    len_sorted_arr = len(list_left) + len(list_right)
    sorted_arr = []
    left_index, right_index = 0, 0
    while len(sorted_arr) < len_sorted_arr:
        if not list_left:
            return list_right
        if not list_right:
            return list_left
        if list_left[left_index] < list_right[right_index]:
            sorted_arr.append(list_left[left_index])
            left_index += 1
        else:
            sorted_arr.append(list_right[right_index])
            right_index += 1
        if left_index == len(list_left):
            sorted_arr += list_right[right_index:]
        elif right_index == len(list_right):
            sorted_arr += list_left[left_index:]
    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left, right = split(arr)
    return merge_sorted_arr(merge_sort(left), merge_sort(right))

print(merge_sort([10, 9, 8, 7, 5, 2, 3, 1, 6, 11]))