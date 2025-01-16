class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlength = 0
        restart = False
        for char in s:
            if char != " ":
                if restart:
                    wordlength = 0
                    restart = False
                wordlength += 1
            if char == " ":
                restart = True
        return wordlength


        