class NumberContainers:

    def __init__(self):
        self.IndexToNumber = {}
        self.NumberToIndexes = collections.defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.IndexToNumber:
            _number = self.IndexToNumber[index]
            self.NumberToIndexes[_number].remove(index)
        self.IndexToNumber[index] = number
        self.NumberToIndexes[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.NumberToIndexes or len(self.NumberToIndexes[number]) == 0:
            return -1
        return self.NumberToIndexes[number][0]

                


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)