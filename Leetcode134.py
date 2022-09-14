from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        currentStart = None
        currentGas = currentLocation = 0
        while currentLocation < n * 2:
            if not currentStart:
                currentStart = currentLocation
            currentGas += gas[currentLocation % n] - cost[currentLocation % n]
            if currentGas < 0:
                currentStart = None
                currentGas = 0
            currentLocation += 1
            if currentStart and currentLocation - currentStart == n:
                return currentStart % n
        return -1


solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(solution.canCompleteCircuit([3, 1, 1], [1, 2, 2]))
