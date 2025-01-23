class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        column_servers = [0] * columnCount
        row_servers = [0] * rowCount
        servers = []
        count = 0
        for row in range(rowCount):
            for column in range(columnCount):
                if grid[row][column] == 1:
                    column_servers[column] += 1
                    row_servers[row] += 1
                    servers.append((row,column))
        for server in servers:
            row,column = server
            if row_servers[row] > 1 or column_servers[column] > 1:
                count += 1
        return count

