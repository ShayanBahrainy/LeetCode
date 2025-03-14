class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        while left <= right:
            mid = (left + right) // 2
            if self.canGiveAmount(candies, mid, k):
                left = mid + 1
            else:
                right = mid - 1
        return right if right > 0 else 0
    def canGiveAmount(self, candies, amount, k):
        quantity = 0
        for candy in candies:
            if candy >= amount:
                quantity += candy // amount
        if quantity >= k:
            return True
        return False
        