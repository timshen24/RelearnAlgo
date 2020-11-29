def split(array):
    mid = len(array) // 2
    return array[:mid], array[mid:]


def merge_sorted_array(list_left, list_right):
    if not list_left:
        return list_right
    if not list_right:
        return list_left
    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] < list_right[index_right]:
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1
        if index_left == len(list_left):
            list_merged += list_right[index_right:]
            break
        elif index_right == len(list_right):
            list_merged += list_left[index_left:]
            break
    return list_merged

def merge_sort(array):
    if len(array) < 2:
        return array
    left, right = split(array)
    return merge_sorted_array(merge_sort(left), merge_sort(right))

print(merge_sort([9, 1, 10, 2]))
