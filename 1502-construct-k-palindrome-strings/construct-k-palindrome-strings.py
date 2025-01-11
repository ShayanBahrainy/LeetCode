class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odds = 0
        char_map = self.character_frequency(s)
        for i in range(26):
            if char_map[i] % 2 > 0:
                odds += 1
        
        return odds <= k
    def character_frequency(self, s: str):
        char_map  = {}
        for char in s:
            if not char_map.__contains__(char):
                char_map[char] = 1
            else:
                char_map[char] += 1
        r = []
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if not char_map.__contains__(char):
                r.append(0)
            else:
                r.append(char_map[char])
        return r