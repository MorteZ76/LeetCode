class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
            out_string = []
            if n == 0 :
                return [""]
            if n == 1 :
                return ["()"]
            for i in range(n) :
                s_open = ["("]
                s_close =[")"]
                list1= s_open
                list2 = self.generateParenthesis(i)
                list3 = s_close 
                list4 = self.generateParenthesis(n-i -1)
                out_string.extend(self.concat4Strings(list1, list2, list3, list4))
            return out_string
    
    def concat4Strings (self, list1, list2, list3, list4) :
        out_concat = [] 
        for s1 in list1 :
            for s2 in list2 :
                for s3 in list3 :
                    for s4 in list4 :
                        concated_s = ""
                        concated_s = concated_s + s1 + s2 + s3 + s4 
                        out_concat.append(concated_s)
        return out_concat
