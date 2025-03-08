class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m = self.countWs(blocks[:k])
        for i in range(0, len(blocks) - k + 1):
            m = min(m, self.countWs(blocks[i: i + k]))
        return m

    @staticmethod
    def countWs(s):
        r = 0
        for c in s:
            if c == "W":
                r += 1
        return r
