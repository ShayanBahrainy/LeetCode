class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        combinations = set()
        def generateCombinations(current, counter):
            combinations.add(current)
            if len(current) == len(tiles):
                return
            for letter in counter:
                if counter[letter] == 0:
                    continue
                current_m = current + letter
                counter_m = counter.copy()
                counter_m[letter] -= 1
                generateCombinations(current_m, counter_m)
        generateCombinations("", counter)
        return len(combinations) - 1

