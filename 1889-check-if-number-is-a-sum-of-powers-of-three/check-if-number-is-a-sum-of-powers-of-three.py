class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        used = set()
        x = 16
        while x > -1 and n != 2:
            if 3 ** x <= n and x not in used:
                n -= 3 ** x
                used.add(x)
            x -= 1
        if n == 0:
            return True
        return False