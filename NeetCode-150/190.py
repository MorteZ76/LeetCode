class Solution:
    def reverseBits(self, n: int) -> int:
        bits = f'{n:032b}'
        final_num = 0
        current_bit = 1 
        for i in range (len(bits)) :
            if (bits[i] == '1') :
                final_num += current_bit 
            current_bit  *= 2
        return final_num


        