from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
        prev_digit = {v: k for k, v in next_digit.items()}
        visited = set(deadends)
        if '0000' in visited:
            return -1
        queue = deque(["0000"])
        step = 0
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                top = queue.popleft()
                if top == target:
                    return step
                for i in range(4):
                    combo = top[:i] + next_digit[top[i]] + top[i+1:]
                    if combo not in visited:
                        queue.append(combo)
                        visited.add(combo)
                    combo = top[:i] + prev_digit[top[i]] + top[i+1:]
                    if combo not in visited:
                        queue.append(combo)
                        visited.add(combo)
            step += 1
        return -1


solution = Solution()
print(solution.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
print(solution.openLock(deadends=["8888"], target="0009"))
