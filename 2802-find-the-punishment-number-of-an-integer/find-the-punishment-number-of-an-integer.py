class Solution:
    def can_partition(self, num, target):
        if target < 0 or num < target:
            return False

        if num == target:
            return True

        return (self.can_partition(num // 10, target - num % 10) or self.can_partition(num // 100, target - num % 100) or self.can_partition(num // 1000, target - num % 1000))
    def punishmentNumber(self, n: int) -> int:
        punishmentNum = 0
        for i in range(1, n + 1):
            square_i = i * i
            if self.can_partition(square_i, i):
                punishmentNum += square_i
        return punishmentNum