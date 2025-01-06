class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        digits = "0123456789"
        v = [0] * (len(s) + 1)
        lastindex = 0
        for i,char in enumerate(s):
            if char == "-" and i == 0:
                sign = -1
                continue
            if char == "+" and i == 0:
                continue
            if char not in digits:
                break
            v[i] = int(char) + (v[i - 1] * 10)
            lastindex = i
        return max(min(v[lastindex] * sign, 2**31-1),-2**31)
            
            