class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        out.append(0)
        i = 1
        while i <= n: 
            if i % 2 ==1 :
                out.append(out[int((i-1)/2)] + 1)
            else :
                out.append(out[int((i)/2)])
            i += 1
        return out 
        