from typing import List
from collections import deque

next_digit = {**{str(i): str(i+1) for i in range(9)}, "9":"0"}
prev_digit = {v: k for k, v in next_digit.items()}


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    visited = set(trapped_combos)
    queue = deque(["0000"])
    step = 0
    while queue:
        qLen = len(queue)
        for _ in range(qLen):
            top = queue.popleft()
            for i in range(4):
                combo = top[:i] + next_digit[top[i]] + top[i + 1:]
                if combo == target_combo:
                    print(f"next_digit: {combo}")
                    return step
                if combo not in visited:
                    queue.append(combo)
                if top not in visited:
                    visited.add(combo)
                combo = top[:i] + prev_digit[top[i]] + top[i + 1:]
                if combo == target_combo:
                    print(f"prev_digit: {combo}")
                    return step
                if combo not in visited:
                    queue.append(combo)
                if top not in visited:
                    visited.add(combo)
        step += 1
    return step