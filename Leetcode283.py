class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for i in range(0, len(nums)-1):
            if j==len(nums):
                break
            while nums[j] == 0:
                j+=1
            if nums[i]!=0:
                i+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

if __name__ == '__main__':
    solution=Solution()
    nums=[0,0]
    solution.moveZeroes(nums)
    print(nums)