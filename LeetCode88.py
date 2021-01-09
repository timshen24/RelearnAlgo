import typing as List
class Solution:
    def merge(self, nums1: List, m: int, nums2: List, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        for i in range(len(nums1) - 1, -1, -1):
            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
            if m == 0:
                print(f'{nums2[:n]}, {n}')
                nums1[:n] = nums2[:n]
            if n == 0:
                break

if __name__ == '__main__':
    solution = Solution()
    nums1, nums2 = [2, 0], [1]
    solution.merge([2, 0], 1, [1], 1)
    print(nums1)