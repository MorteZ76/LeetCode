class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set () 
        left = 0 
        right = 0 
        mx = 0
        while right < len(s) :
            if s[right] in current_chars: 
                while s[left] != s[right] :
                    current_chars.discard(s[left])
                    left += 1 
                left += 1
            else :
                current_chars.add(s[right]) 
                mx = max(mx, right - left + 1)
            right += 1
        return mx
            