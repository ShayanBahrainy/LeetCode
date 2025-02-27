class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        maxLen = 0
        for i in range(len(arr)):
            start = arr[i]
            for j in range(i + 1, len(arr)):
                after = arr[j]
                queue = deque()
                queue.append(start)
                queue.append(after)
                length = 2
                while (queue[0] + queue[1]) in nums:
                    queue.append(queue[0] + queue[1])
                    queue.popleft()
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen if maxLen != 2 else 0
        