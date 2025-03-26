class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        numbers = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        numbers.sort()
        length = len(numbers)
        median = numbers[length // 2]
        ops = 0
        for num in numbers:
            if num % x != median % x:
                return -1
            ops += abs(median - num) / x
        return int(ops)