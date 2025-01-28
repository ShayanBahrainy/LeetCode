class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions_modifier = [1, -1, 0]
        possible_fishes = [0]
        starting_indexes = []
        rows = len(grid)
        columns = len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    starting_indexes.append((r,c))
        possible_fishes.append(0)
        visited = set()
        for index in starting_indexes:
            if index in visited:
                continue
            queue = [index]
            possible_fish = 0
            while queue:
                r,c = queue.pop()
                for dr in directions_modifier:
                    if (r + dr,c ) in visited:
                        continue
                    if not self._is_valid_(rows, columns, r + dr, c):
                        continue
                    if grid[r + dr][c] > 0:
                        possible_fish += grid[r + dr][c]
                        queue.append((r + dr,c))
                        visited.add((r + dr, c))
                for dc in directions_modifier:
                    if (r,c + dc) in visited:
                        continue
                    if not self._is_valid_(rows, columns, r, c + dc):
                        continue
                    if grid[r][c + dc] > 0:
                        possible_fish += grid[r][c + dc]
                        queue.append((r,c + dc))
                        visited.add((r, c + dc))    
            possible_fishes.append(possible_fish)
        max_fish = 0
        for possible_fish in possible_fishes:
            max_fish = max(max_fish, possible_fish)
        return max_fish
    def _is_valid_(self, rows, columns, row, column):
        if (row < 0) or (row > (rows - 1)):
            return False
        if (column < 0) or (column > (columns - 1)):
            return False
        return True
