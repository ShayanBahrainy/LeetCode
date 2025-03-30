class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrence = [-1] * 26
        for i in range(len(s)):
            char = s[i]
            lastOccurrence[ord(char) - ord("a")] = i
        partitionStart, partitionEnd = 0, 0
        partitionSizes = []
        for i in range(len(s)):
            partitionEnd = max(partitionEnd, lastOccurrence[ord(s[i]) - ord("a")])
            if i == partitionEnd:
                partitionSizes.append(i - partitionStart + 1)
                partitionStart = i + 1
        return partitionSizes