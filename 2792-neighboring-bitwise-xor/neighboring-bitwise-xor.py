class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        r = 0
        for i in range(0, len(derived)):
            r ^= derived[i]
        return r == 0