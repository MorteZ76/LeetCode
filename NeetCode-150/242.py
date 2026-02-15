class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        different_letters = set()
        for i in range (len(s)) :
            if not (s[i] in different_letters) :
                different_letters.add(s[i])
        if len(s) != len(t) :
            return False
        for i in different_letters:
            if s.count(i) != t.count(i) :
                return False
        return True 
        