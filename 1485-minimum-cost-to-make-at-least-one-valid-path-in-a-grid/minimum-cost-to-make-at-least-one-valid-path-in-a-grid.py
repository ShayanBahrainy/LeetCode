class Solution:
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    def minCost(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        minCost = [[float("inf")] * numCols for _ in range(numRows)]
        deque = collections.deque([(0,0)])
        deque.append([0,0])
        minCost[0][0] = 0
        while deque:
            row, col = deque.popleft()

            for dir_idx, (dx, dy) in enumerate(self.directions):
                new_row, new_col = row + dx, col + dy
                cost = 0 if grid[row][col] == dir_idx + 1 else 1
                if (self.isValid(new_row, new_col, numRows, numCols)) and (minCost[row][col] + cost) < minCost[new_row][new_col]:
                    minCost[new_row][new_col] = minCost[row][col] + cost
                    if cost == 1:
                        deque.append((new_row,new_col))
                    else:
                        deque.appendleft((new_row, new_col))
        return minCost[numRows - 1][numCols - 1]

    def isValid(self, row, col, numRows, numCols) -> bool:
        if row < 0 or row > numRows - 1:
            return False
        if col < 0 or col > numCols - 1:
            return False
        return True