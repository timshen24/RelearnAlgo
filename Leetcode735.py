from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid >= 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and asteroid < 0:
                    prev = stack.pop()
                    if prev + asteroid == 0:
                        asteroid = 0
                    elif prev + asteroid > 0:
                        asteroid = prev
                if asteroid:
                    stack.append(asteroid)
        return stack


solution = Solution()
# print(solution.asteroidCollision([5, 10, -5, 2, 3, -5]))
print(solution.asteroidCollision([-2, -1, 1, 2]))
