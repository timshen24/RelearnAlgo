import heapq


# Brute force
def nth_ugly_number(n: int) -> int:
    ugly_numbers = []
    i = 1
    max_int = 2147483647
    while i <= max_int:
        j = i
        while j <= max_int:
            k = j
            while k <= max_int:
                ugly_numbers.append(k)
                k *= 5
            j *= 3
        i *= 2
    ugly_numbers.sort()
    return ugly_numbers[n - 1]


print(nth_ugly_number(10))


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        allowed_primes = [2, 3, 5]
        used_nums = {1}
        for i in range(n - 1):
            uglyNum = heapq.heappop(heap)
            for prime in allowed_primes:
                nextUglyNum = uglyNum * prime
                if nextUglyNum not in used_nums:
                    used_nums.add(nextUglyNum)
                    heapq.heappush(heap, nextUglyNum)
        return heap[0]


solution = Solution()
solution.nthUglyNumber(10)
