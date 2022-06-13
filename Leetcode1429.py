class Solution:
    nums = []
    d = {}

    def add(self, num):
        self.nums.append(num)
        self.d[num] = self.d.get(num, 0) + 1

    def find_first_non_repeated_num(self):
        if not self.nums:
            return -1
        while len(self.nums):
            if self.d.get(self.nums[0], 0) == 1:
                return self.nums[0]
            self.nums.pop(0)
        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.add(3)
    solution.add(1)
    solution.add(2)
    print(solution.find_first_non_repeated_num())
    solution.add(3)
    print(solution.find_first_non_repeated_num())
    solution.add(1)
    solution.add(2)
    print(solution.find_first_non_repeated_num())