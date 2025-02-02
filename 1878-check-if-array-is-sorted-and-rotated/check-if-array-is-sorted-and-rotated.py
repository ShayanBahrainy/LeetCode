class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)

        sorted_copy = sorted(nums)

        for rotationOffset in range(length):
            is_match = True
            for i in range(length):
                if nums[(rotationOffset + i) % length] != sorted_copy[i]:
                    is_match = False
                    break
            if is_match:
                return True
        return False
                