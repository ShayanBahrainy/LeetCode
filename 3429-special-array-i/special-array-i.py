class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        lastNumber = -1
        for num in nums:
            if num % 2 == lastNumber:
                return False
            lastNumber = num % 2
        return True