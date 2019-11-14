from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def backtrack(index, total):
            if total == target:
                res.append(path.copy())
                return
            if index == len(candidates):
                return
            for i in range(index, len(candidates)):
                total += candidates[i]
                if total > target:
                    return
                path.append(candidates[i])
                backtrack(i + 1, total)
                total -= candidates[i]
                path.pop()
            return
        backtrack(0, 0)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))