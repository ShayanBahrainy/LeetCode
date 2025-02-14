class ProductOfNumbers:

    def __init__(self):
        self.nums = deque()

    def add(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.appendleft(num)
        else:
            self.nums.appendleft(num * self.nums[0])
        if num == 0:
            self.nums = deque()
    def getProduct(self, k: int) -> int:
        if len(self.nums) < k:
            return 0
        if len(self.nums) == k:
            return int(self.nums[0])
        return int(self.nums[0] / self.nums[k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)