class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        key_to_sum = {}
        for nums in nums1:
            key_to_sum[nums[0]] = nums[1]
        for nums in nums2:
            key_to_sum[nums[0]] = key_to_sum.get(nums[0], 0) + nums[1]
        result = []
        for k, v in sorted(key_to_sum.items()):
            result.append([k, v])
        return result