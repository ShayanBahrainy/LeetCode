class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits_two = 0

        twos_binary = bin(num2)[2:]
        ones_binary = bin(num1)[2:]

        set_twos = self.bitCount(twos_binary)
        set_ones = self.bitCount(ones_binary)

        if set_ones == set_twos:
            return num1
        res = num1
        for i in range(32):
            if set_ones  > set_twos and (1 << i) & num1 > 0:
                res ^= 1 << i
                set_ones -= 1
            if set_ones < set_twos and (1 << i) & num1 == 0:
                res ^= 1 << i
                set_ones += 1
        return res

    def bitCount(self, number: str) -> int:
        value = 0
        for char in number:
            if char == '1':
                value += 1
        return value


            