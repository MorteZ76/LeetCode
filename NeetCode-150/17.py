class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        if len(digits) == 1:
            match digits[0] :
                case "2" :
                    out = ["a","b","c"]
                case "3" :
                    out = ["d","e","f"]
                case  "4" :
                    out = ["g","h","i"]
                case  "5" :
                    out = ["j","k","l"]
                case "6" :
                    out = ["m","n","o"]
                case "7" :
                    out = ["p","q","r","s"]
                case "8" :
                    out = ["t","u","v"]
                case "9" :
                    out = ["w","x","y","z"]
        else : 
            list1 = self.letterCombinations(digits[0])
            list2 = self.letterCombinations(digits[1:])
            for s1 in list1:
                for s2 in list2:
                    s3 = s1 + s2
                    out.append(s3)
        
        return out

        