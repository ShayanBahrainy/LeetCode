class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key in count:
            if count[key] % 2 != 0:
                return False
        return True