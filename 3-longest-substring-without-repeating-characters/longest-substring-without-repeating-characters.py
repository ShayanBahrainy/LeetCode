class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 1
        seen = []
        for char in s:
            if char in seen:
                seen_str = "".join(seen)
                seen = list(seen_str[seen_str.find(char) + 1:])
            seen.append(char)
            maxLen = max(maxLen, len(seen))
        return maxLen
