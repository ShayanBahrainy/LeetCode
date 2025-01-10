class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wordmaps1 = []
        wordmaps2 = []
        results = []
        for word in words1:
            wordmaps1.append(self.wordmap(word))
        for word in words2:
            wordmaps2.append(self.wordmap(word))
        
        word_minimum = self.min_map(wordmaps2[0],"0" * 26)
        for i in range(1,len(wordmaps2)):
            word_minimum = self.min_map(word_minimum, wordmaps2[i])
        for i,word1 in enumerate(wordmaps1):
            if self.is_subset(word_minimum, word1):
                results.append(words1[i])
        return results
            
    def wordmap(self, word):
        wordmap = {}
        r = ""
        for char in word:
            if not wordmap.__contains__(char):
                wordmap[char] = 1
            else:
                wordmap[char] += 1
        for char in 'abcdefghijklmnopqrstuvwxyz':
            r += str(wordmap[char] if wordmap.__contains__(char) else 0)
        return r 
    def is_subset(self, sub: str, dom: str) -> bool:
        "Check if sub is a subset of dom, arguments are the word map of both strings."
        for i in range(26):
            if int(sub[i]) > int(dom[i]):
                return False
        return True
    def min_map(self,a: str, b: str) -> str:
        "Go through the maps of the strings, and keep whichever value is lower for each position"
        r = ""
        for i in range(26):
            r += str(max(int(a[i]),int(b[i])))
        return r