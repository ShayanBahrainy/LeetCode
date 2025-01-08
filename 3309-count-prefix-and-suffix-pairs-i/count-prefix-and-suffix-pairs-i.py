class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for pre,word in combinations(words,2):
            count += int(word.startswith(pre) and word.endswith(pre))
        return count