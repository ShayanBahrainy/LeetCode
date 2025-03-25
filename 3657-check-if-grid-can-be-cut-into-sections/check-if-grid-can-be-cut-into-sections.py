class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return Solution.checkCuts(rectangles, 0) or Solution.checkCuts(rectangles, 1)
    @staticmethod
    def checkCuts(rectangles, dim):
        gap_count = 0
        rectangles.sort(key=lambda rect: rect[dim])
        furthest_end = rectangles[0][dim + 2]
        for i in range(1, len(rectangles)):
            rect = rectangles[i]
            if furthest_end <= rect[dim]:
                gap_count += 1
            if gap_count == 2:
                return True
            furthest_end = max(furthest_end, rect[dim + 2])
        return gap_count >= 2