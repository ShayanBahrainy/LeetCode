class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        difference_array = [0 for _ in range(len(nums) + 1)]
        for query in queries:
            difference_array[query[0]] += 1
            difference_array[query[1] + 1] -= 1
        for i in range(1, len(difference_array)):
            difference_array[i] += difference_array[i - 1]
        for i in range(len(nums)):
            if difference_array[i] < nums[i]:
                return False
        return True
