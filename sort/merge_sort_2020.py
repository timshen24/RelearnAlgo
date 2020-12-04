def split(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def merge_sorted_list(left_list, right_list):
    if not left_list:
        return right_list
    if not right_list:
        return left_list
    left_index=right_index=0
    merged_list = []
    len_merged_list = len(left_list) + len(right_list)
    while len(merged_list) <= len_merged_list:
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
        if left_index == len(left_list):
            merged_list += right_list[right_index:]
            break
        elif right_index == len(right_list):
            merged_list += left_list[left_index:]
            break
    return merged_list

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left, right = split(arr)
    return merge_sorted_list(merge_sort(left), merge_sort(right))

print(merge_sort([9, 1, 10, 2]))
