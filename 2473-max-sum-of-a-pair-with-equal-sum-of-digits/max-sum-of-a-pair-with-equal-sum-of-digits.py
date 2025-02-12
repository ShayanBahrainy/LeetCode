class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        SumMaps = DefaultDict(SortedList)
        for i in range(len(nums)):
            digitSum = 0
            for digit in str(nums[i]):
                digitSum += int(digit)
            SumMaps[digitSum].add(nums[i])
        MaxSum = -1
        for Sum in SumMaps:
            NumbersWithSum = SumMaps[Sum]
            if len(NumbersWithSum) > 1:
                MaxSum = max(NumbersWithSum[-1] + NumbersWithSum[-2], MaxSum)
        return MaxSum