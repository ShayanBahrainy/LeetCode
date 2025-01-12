class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opens = []
        closes = 0
        available = []
        for i in range(len(locked)):
            if locked[i] == '0':
                available.append(i)
            elif s[i] == '(':
                opens.append(i)
            elif s[i] == ')':
                if len(opens) > 0:
                    opens.pop(-1)
                elif len(available) > 0:
                    available.pop(-1)
                else:
                    return False
        while len(opens) > 0 and len(available) > 0 and opens[-1] < available[-1]:
            opens.pop(-1)
            available.pop(-1)
        if len(opens) > 0:
            return False
        return True