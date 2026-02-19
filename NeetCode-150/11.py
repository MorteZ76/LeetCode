class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) -1
        mx_area = 0
        while right > left :
            if min(height[left],height[right]) * (right - left) > mx_area  :
                mx_area =  min(height[left],height[right]) * (right - left) 
            if height[left] > height[right] :
                right -= 1
            else :
                left += 1
        return mx_area