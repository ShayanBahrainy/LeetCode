class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows_count = len(mat)
        cols_count = len(mat[0])
        positions = {}
        for i in range(rows_count):
            for j in range(cols_count):
                positions[mat[i][j]] = (i,j)
        cols = {}
        rows = {}
        for index in range(len(arr)):
            j,i = positions[arr[index]]
            cols[i] = cols.get(i, 0) + 1
            rows[j] = rows.get(j, 0) + 1
            if rows[j] == cols_count:
                return index
            if cols[i] == rows_count:
                return index
        