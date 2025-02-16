from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * (2 * n - 1)
        vis = [False] * (n + 1)
        def solve(indx: int, count: int) -> bool:
            if count == 2 * n - 1:
                return True
            if seq[indx]:
                return solve(indx + 1, count)
            for i in range(n, 0, -1):
                if not vis[i]:
                    if i == 1:
                        vis[i] = True
                        seq[indx] = i
                        if solve(indx + 1, count + 1):
                            return True
                        vis[i] = False
                        seq[indx] = 0
                    elif indx + i < len(seq) and not seq[indx + i]:
                        vis[i] = True
                        seq[indx] = i
                        seq[indx + i] = i
                        if solve(indx + 1, count + 2):
                            return True
                        vis[i] = False
                        seq[indx] = 0
                        seq[indx + i] = 0
            return False
        solve(0, 0)

        return seq