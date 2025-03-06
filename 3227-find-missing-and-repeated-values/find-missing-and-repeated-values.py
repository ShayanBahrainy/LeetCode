class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        used = set()
        needed = set(range(1, (len(grid) ** 2 + 1)))
        result = [0, 0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in used:
                    result[0] = grid[i][j]
                used.add(grid[i][j])
        for thing in needed - used:
            result[1] = thing
        return result