class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_asc_value = nums[0]
        maximum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                current_asc_value += nums[i]
            else:
                current_asc_value = nums[i]
            maximum = max(maximum, current_asc_value)
        return maximum
            
