class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dRow = [0,0,-1,1]
        dCol = [-1, 1, 0, 0]
        numOfRows = len(heightMap)
        numOfCols = len(heightMap[0])
        visited = [([False] * numOfCols) for _ in range(numOfRows)]
        boundary = []

        for i in range(numOfRows):
            heapq.heappush(boundary, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, self.Cell(heightMap[i][numOfCols - 1], i, numOfCols - 1))
            visited[i][0] = visited[i][numOfCols - 1] = True
        for i in range(numOfCols):
            heapq.heappush(boundary, self.Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary, self.Cell(heightMap[numOfRows - 1][i], numOfRows -1, i))
            visited[0][i] = visited[numOfRows - 1][i] = True
        total_water_volume = 0
        while boundary:
            current_cell = heapq.heappop(boundary)

            current_row = current_cell.x
            current_col = current_cell.y
            min_boundary_height = current_cell.height

            for direction in range(4):
                neighbor_row = current_row + dRow[direction]
                neighbor_col = current_col + dCol[direction]
                if (self._is_valid_cell(neighbor_row, neighbor_col, numOfRows, numOfCols) and not visited[neighbor_row][neighbor_col]):
                    neighbor_height = heightMap[neighbor_row][neighbor_col]
                    if neighbor_height < min_boundary_height:
                        total_water_volume += min_boundary_height - neighbor_height
                    heapq.heappush(boundary, self.Cell(max(neighbor_height,min_boundary_height), neighbor_row, neighbor_col),)
                    visited[neighbor_row][neighbor_col] = True
        return total_water_volume
    def _is_valid_cell(self, row, col, numOfRows, numOfCols):
        if (row <= 0 or row >= numOfRows) or (col <= 0 or col >= numOfCols):
            return False
        return True
    class Cell:
        def __init__(self, height, x, y):
            self.height = height
            self.x = x
            self.y = y
        def __lt__(self, other):
            return self.height < other.height
