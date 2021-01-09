def split(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def merge_sorted_array(list_left, list_right):
    left_index, right_index = 0, 0
    len_sorted_list = len(list_left) + len(list_right)
    sorted_arr = []
    while len(sorted_arr) < len_sorted_list:
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
    return merge_sorted_array(merge_sort(left), merge_sort(right))

print(merge_sort([9, 1, 10, 2]))
