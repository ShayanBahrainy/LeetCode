class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        strings = []
        for i1 in range(len(words)):
            for i2 in range(len(words)):
                if i1 == i2:
                    continue
                if not words[i1] in words[i2]:
                    continue
                if words[i1] in strings:
                    continue
                strings.append(words[i1])
        return strings
