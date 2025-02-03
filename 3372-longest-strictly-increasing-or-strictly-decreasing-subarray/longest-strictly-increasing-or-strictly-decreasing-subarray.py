class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        ascending = 1
        descending = 1
        max_movement = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ascending += 1
                descending = 1
            elif nums[i] < nums[i - 1]:
                descending += 1
                ascending = 1
            else:
                descending = 1
                ascending = 1

            max_movement = max(max(ascending, descending), max_movement)
        return max_movement
        
