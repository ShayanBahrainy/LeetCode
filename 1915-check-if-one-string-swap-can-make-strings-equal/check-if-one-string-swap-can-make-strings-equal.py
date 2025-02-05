class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        switchIndexes = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                switchIndexes.append(i)
        if len(switchIndexes) == 0:
            return True
        if len(switchIndexes) != 2:
            return False
        i1 = switchIndexes[0]
        i2 = switchIndexes[1]
        print(switchIndexes)
        if s1[i2] == s2[i1] and s2[i2] == s1[i1]:
            return True
        return False