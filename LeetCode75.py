from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, first, two = -1, 0, len(nums)
        while first < two:
            if nums[first] == 0:
                zero += 1
                nums[first], nums[zero] = nums[zero], nums[first]
                first += 1
            elif nums[first] == 2:
                two -= 1
                nums[first], nums[two] = nums[two], nums[first]
            else:
                first += 1
        return


if __name__ == '__main__':
    solution=Solution()
    nums=[2,0,1]
    solution.sortColors(nums)
    print(nums)
    nums=[2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums)