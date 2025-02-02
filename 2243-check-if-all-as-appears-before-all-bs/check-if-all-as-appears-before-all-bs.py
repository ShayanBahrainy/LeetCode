class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False
        for char in s:
            if char == 'b':
                seenB = True
            if char == 'a' and seenB == True:
                return False
        return True
