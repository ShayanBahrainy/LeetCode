class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float("inf")
        for turning_point in range(len(grid[0])):
            first_row_sum -= grid[0][turning_point]
            minimum_sum = min(max(first_row_sum, second_row_sum), minimum_sum)
            second_row_sum += grid[1][turning_point]
        return minimum_sum