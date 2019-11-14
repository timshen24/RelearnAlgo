from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for i in range(len(nums))]
        res = []
        path = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    used[i] = False
                    path.pop()
            return
        backtrack()
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))