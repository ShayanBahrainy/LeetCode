class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        found = True
        while found:
            found = False
            index = s.find(part)
            if index != -1:
                found = True
                s = s[:index] + s[index + len(part): ]
        return s