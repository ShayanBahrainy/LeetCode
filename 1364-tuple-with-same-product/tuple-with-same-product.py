class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_pairs = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                num1 = nums[i]
                num2 = nums[j]
                if not product_pairs.__contains__(num1 * num2):
                    product_pairs[num1 * num2] = set()
                product_pairs[num1 * num2].add((num1, num2))
        unique = 0
        for product in product_pairs:
            used_numbers = set()
            duplicates_removed = product_pairs[product].copy()
            for pair in product_pairs[product]:
                if pair[0] not in used_numbers and pair[1] not in used_numbers:
                    used_numbers.add(pair[0])
                    used_numbers.add(pair[1])
                else:
                    duplicates_removed.discard(pair)
            pairs = len(duplicates_removed)
            unique += (pairs * (pairs - 1)) * 4
        return unique
