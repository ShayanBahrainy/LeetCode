class Solution:
    def clearDigits(self, s: str) -> str:
        nums = "1234567890"
        doneChange = True
        while doneChange == True:
            doneChange = False
            i = 0
            while i < len(s) - 1:
                char1 = s[i]
                char2 = s[i + 1]
                if char1 not in nums and char2 in nums:
                    s = s[:i] + s[i + 2:]
                    doneChange = True
                i += 1
        return s