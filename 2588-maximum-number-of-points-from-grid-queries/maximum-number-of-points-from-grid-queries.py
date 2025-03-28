class Solution:
    ROW_DIRECTIONS = [0, 0, 1, -1]
    COL_DIRECTIONS = [1, -1, 0, 0]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count, col_count = len(grid), len(grid[0])
        total_cells = row_count * col_count
        sorted_queries = [Query(i, val) for i, val in enumerate(queries)]
        sorted_queries.sort(key=lambda x: x.value)
        sorted_cells = [Cell(row, col, grid[row][col]) for row in range(row_count) for col in range(col_count)]
        sorted_cells.sort(key=lambda x: x.value)
        uf = UnionFind(total_cells)
        result = [0] * len(queries)

        cell_index = 0
        for query in sorted_queries:
            while (cell_index < total_cells and sorted_cells[cell_index].value < query.value):
                row = sorted_cells[cell_index].row
                col = sorted_cells[cell_index].col
                cell_id = (row * col_count + col)
                for direction in range(4):
                    new_row = row + Solution.ROW_DIRECTIONS[direction]
                    new_col = col + Solution.COL_DIRECTIONS[direction]
                    if (0 <= new_row < row_count and 0 <= new_col < col_count and grid[new_row][new_col] < query.value):
                        uf.union(cell_id, new_row * col_count + new_col)
                cell_index += 1
            result[query.index] = (uf.get_size(0) if query.value > grid[0][0] else 0)
        return result
                
class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
class Query:
    def __init__(self, index, value):
        self.index = index
        self.value = value
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n
    def find(self, node):
        if self.parent[node] < 0:
            return node
        return self.find(self.parent[node])
    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        if rootA == rootB:
            return False
        
        if self.size[rootA] > self.size[rootB]:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        return True
    def get_size(self, node):
        return self.size[self.find(node)]
