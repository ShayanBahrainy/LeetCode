class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = [0] * (len(nums) + 2)
        ops = 0
        for i in range(len(nums)):
            if (nums[i] == flips[i] % 2):
                ops += 1
                if not i <= len(nums) - 3:   
                    i -= i - (len(nums) - 3)
                flips[i] += 1
                flips[i + 1] += 1
                flips[i + 2] += 1
        for i in range(len(nums)):
            if nums[i] == (flips[i] % 2):
                return -1
        return ops
             
