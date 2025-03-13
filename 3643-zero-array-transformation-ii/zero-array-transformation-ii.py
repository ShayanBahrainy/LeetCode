class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)
        if not self.isValid(nums, right, queries):
            return -1
        while left <= right:
            mid = left + (right - left) // 2
            if self.isValid(nums, mid, queries):
                right = mid - 1
            else:
                left = mid + 1
        return left
    def isValid(self, nums, k, queries) -> bool:
        subArr = [0]  * (len(nums) + 1)
        for i in range(k):
            query = queries[i]
            subArr[query[0]] += query[2]
            subArr[query[1] + 1] -= query[2]
        
        for i in range(1, len(subArr)):
            subArr[i] += subArr[i - 1]

        for i in range(len(subArr) - 1):
            if nums[i] > subArr[i]:
                return False
        return True
