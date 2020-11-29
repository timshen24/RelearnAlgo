from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,0,len(nums)-1
        while j<=k:
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            elif nums[j]==2:
                nums[j],nums[k]=nums[k],nums[j]
                k-=1
            else:
                j+=1
        return


if __name__ == '__main__':
    solution=Solution()
    nums=[2,0,1]
    solution.sortColors(nums)
    print(nums)
    nums=[2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums)