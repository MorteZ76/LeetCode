class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = f'{n:032b}'
        return bits.count('1')
        