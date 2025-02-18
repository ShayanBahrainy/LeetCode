class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9])
        used = set()
        pattern = "I" + pattern
        Following_Ds = [0] * len(pattern)
        lastincrease = -1
        result = ""
        for i in range(len(pattern)):
            if pattern[i] == "I":
                lastincrease = i
            if pattern[i] == "D":
                Following_Ds[lastincrease] += 1
        for i in range(len(pattern)):
            if pattern[i] == "I":
                nextNum = (nums - used)[0] + Following_Ds[i]
            if pattern[i] == "D":
                nextNum = int(result[-1]) - 1
            result += str(nextNum)
            used.add(nextNum) 
        return result