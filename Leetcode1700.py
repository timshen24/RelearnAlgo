from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = 0
        i = 0
        while students:
            if students[0] == sandwiches[0]:
                i = 0
                students.pop(0)
                sandwiches.pop(0)
                res += 1
            else:
                v = students.pop(0)
                students.append(v)
                i += 1
                if i == len(students):
                    break
        return len(students)


solution = Solution()
print(solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
