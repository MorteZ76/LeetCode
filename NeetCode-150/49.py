class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        unique_strings = {}
        for i in range (len(strs)) :
            str_sorted = "".join(sorted(strs[i]))
            if str_sorted in unique_strings :
                out[unique_strings[str_sorted]].append(strs[i])
            else :
                out.append([strs[i]])
                unique_strings[str_sorted] = len(out) -1
        return out


        