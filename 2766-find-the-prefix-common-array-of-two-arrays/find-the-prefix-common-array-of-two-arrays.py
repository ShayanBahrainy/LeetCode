class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        encountered = []
        common = 0
        prefix_common = [0] * len(A)
        for i in range(len(A)):
            if A[i] in encountered:
                common += 1
            encountered.append(A[i])
            if B[i] in encountered:
                common += 1
            encountered.append(B[i])
            prefix_common[i] = common
        return prefix_common
        