class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        i = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            i += 1
        return i