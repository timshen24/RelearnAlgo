from typing import List


def maximum_score(arr1: List[int], arr2: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    total = p1 = p2 = section_sum1 = section_sum2 = 0
    len1, len2 = len(arr1), len(arr2)
    while p1 < len1 or p2 < len2:
        if p1 < len1 and p2 < len2 and arr1[p1] == arr2[p2]:
            total += max(section_sum1, section_sum2) + arr1[p1]
            section_sum1 = section_sum2 = 0
            p1 += 1
            p2 += 1
        elif p2 == len2 or (p1 < len1 and arr1[p1] < arr2[p2]):
            section_sum1 += arr1[p1]
            p1 += 1
        else:
            section_sum2 += arr2[p2]
            p2 += 1
    return total + max(section_sum1, section_sum2)


if __name__ == '__main__':
    arr1 = [2, 4, 5, 8, 10]
    arr2 = [4, 6, 8, 9]
    res = maximum_score(arr1, arr2)
    print(res)
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [3, 5, 100]
    res = maximum_score(arr1, arr2)
    print(res)
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    res = maximum_score(arr1, arr2)
    print(res)
    arr1 = [1, 4, 5, 6, 12, 14]
    arr2 = [10, 13, 16, 21, 27]
    res = maximum_score(arr1, arr2)
    print(res)
