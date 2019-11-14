from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        total = 0
        city1,city2 = n - 1,n - 1
        for i in range(len(costs)):
            if city1 == -1:
                total += costs[i][1]
            elif city2 == -1:
                total += costs[i][0]
            elif costs[i][0] < costs[i][1]:
                total += costs[i][0]
                city1 -= 1
            else:
                total += costs[i][1]
                city2 -= 1
        return total

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))