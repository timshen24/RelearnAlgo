def split(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def merge_sorted_array(left_list, right_list):
    if not left_list:
        return right_list
    if not right_list:
        return left_list
    left_index, right_index = 0, 0
    len_sorted_arr = len(left_list) + len(right_list)
    sorted_arr = []
    while len(sorted_arr) < len_sorted_arr:
        if left_list[left_index] < right_list[right_index]:
            sorted_arr.append(left_list[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_list[right_index])
            right_index += 1
        if left_index == len(left_list):
            sorted_arr += right_list[right_index:]
        elif right_index == len(right_list):
            sorted_arr += left_list[left_index:]
    return sorted_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left, right = split(arr)
    return merge_sorted_array(merge_sort(left), merge_sort(right))


print(merge_sort([10, 9, 8, 7, 5, 2, 3, 1, 6, 11]))
