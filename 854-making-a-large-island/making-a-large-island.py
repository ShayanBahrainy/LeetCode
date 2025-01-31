class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [1, -1]
        ones = []
        zeroes = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ones.append((i,j))
                else:
                    zeroes.append((i,j))
        connectedIsland = {}
        connectedIslandId = {}
        sizes = []
        visited = set()
        islands = []
        island_id = 0
        for i,j in ones:
            if (i,j) in visited:
                continue
            visited.add((i,j))
            dq = deque([(i,j)])
            size = 1
            island = set()
            island.add((i,j))
            while dq:
                x,y = dq.popleft()
                for d in directions:
                    if not self._is_valid(rows, cols, x + d, y):
                        continue
                    if (x + d, y) in visited:
                        continue
                    if grid[x + d][y] == 1:
                        size += 1
                        visited.add((x + d, y))
                        island.add((x + d, y))
                        dq.appendleft((x + d, y))
                for d in directions:
                    if not self._is_valid(rows, cols, x, y + d):
                        continue
                    if (x, y + d) in visited:
                        continue
                    if grid[x][y + d] == 1:
                        visited.add((x, y + d))
                        island.add((x, y + d))
                        dq.appendleft((x, y + d))
                        size += 1
            for member in island:
                connectedIsland[member] = size
                connectedIslandId[member] = island_id
            island_id += 1

        if len(zeroes) == 0:
            return rows * cols
        zero_values = []
        for i, j in zeroes:
            visited = set()
            connects = 1
            for d in directions:
                ni = i + d
                nj = j
                if not self._is_valid(rows, cols, ni, nj):
                    continue
                if (ni, nj) in connectedIslandId and connectedIslandId[(ni, nj)] in visited:
                    continue
                if (ni,nj) in connectedIsland:
                    connects += connectedIsland[(ni, nj)]
                    visited.add(connectedIslandId[(ni, nj)])
            for d in directions:
                ni = i
                nj = j + d
                if not self._is_valid(rows, cols, ni, nj):
                    continue
                if (ni, nj) in connectedIslandId and connectedIslandId[(ni, nj)] in visited:
                    continue
                if (ni, nj) in connectedIsland:
                    connects += connectedIsland[(ni, nj)]
                    visited.add(connectedIslandId[(ni, nj)])
            zero_values.append(connects)
        max_connects = max(zero_values, default=0)
        return max_connects

            
            

    def _is_valid(self, rows, cols, row, col):
        if row < 0 or row > (rows - 1):
            return False
        if col < 0 or col > (cols - 1):
            return False
        return True


