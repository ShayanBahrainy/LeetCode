class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prefixSum = defaultdict(int)
        prefix_sum = 0
        starter = days
        available = 0
        for meeting in meetings:
            starter = min(starter, meeting[0])
            prefixSum[meeting[0]] += 1
            prefixSum[meeting[1] + 1] -= 1
        available += starter - 1
        for day in sorted(prefixSum.keys()):
            if prefix_sum == 0:
                available += day - starter
            prefix_sum += prefixSum[day]
            starter = day
        available += days - starter + 1
        return available