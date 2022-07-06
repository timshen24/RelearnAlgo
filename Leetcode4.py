from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        lenAll = len1 + len2
        nums = []
        i, j, index = 0, 0, 0
        while True:
            if not nums1:
                nums = nums2
                break
            if not nums2:
                nums = nums1
                break
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            if i == len(nums1):
                nums.extend(nums2[j:])
                break
            if j == len(nums2):
                nums.extend(nums1[i:])
                break
        print(nums)
        if lenAll % 2:
            index = lenAll // 2 + 1
            return nums[index - 1]
        else:
            index = lenAll // 2
            return (nums[index] + nums[index - 1]) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([], [1]))