class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        num_count = len(nums)
        dominant_num, dominant_amount = counter.most_common(1)[0]
        right = dominant_amount
        left = 0
        for i in range(len(nums)):
            if nums[i] == dominant_num:
                left += 1
                right -= 1
            if right > ((num_count - i - 1)//2) and left > ((i + 1)//2):
                return i
        return -1
