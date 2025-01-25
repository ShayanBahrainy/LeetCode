class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sort_nums = sorted(nums)
        num_to_group = {}
        group_to_members = {0: []}
        group_index = 0
        group_to_members[0].append(sort_nums[0])
        num_to_group[sort_nums[0]] = 0
        for i in range(1,len(sort_nums)):
            num = sort_nums[i]
            if abs(sort_nums[i - 1] - num) > limit:
                group_index += 1
            if group_index not in group_to_members:
                group_to_members[group_index] = []
            group_to_members[group_index].append(num)
            num_to_group[num] = group_index
        for i in range(len(nums)):
            num = nums[i]
            group_index = num_to_group[num]
            nums[i] = group_to_members[group_index].pop(0)
        return nums
