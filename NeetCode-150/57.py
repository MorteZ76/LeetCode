# Very Dirty code, but it works. I will clean it up later.
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        out = []
        if not intervals: 
            return [newInterval]
        first = self.binary_search(intervals, newInterval[0]) 
        second = self.binary_search(intervals,newInterval[1]) 
        if first == -1  :
            if second == -1 :
                out.append(newInterval) 
                out = out + intervals 
                return out
            else :
                start = newInterval[0]
                end = max (intervals[second][1], newInterval[1] )
                out.append([start,end])
                out = out + intervals[second+1:]
                return out    
        out = intervals[:first]
        start = intervals[first][0]
        if intervals[first][1] < newInterval[0] :
            out.append(intervals[first])
            start =  newInterval[0]  
        end = max(intervals[second][1], newInterval[1] )
        out.append([start,end])
        out = out + intervals[second+1:]
        return out
               

    def binary_search(self,nums, val) :
                start = 0 
                end = len(nums)- 1
                if (nums[start][0] > val) :
                    return -1
                while (end > start + 1) :
                    mid = (end + start ) // 2
                    if ( nums[mid][0] > val ) :
                        end = mid -1 
                    elif ( nums[mid][0] == val ) :
                         return mid
                    else :
                        start = mid
                if ( nums[end][0] <= val ) :
                        return end
                elif ( nums[start][0] <= val ) :
                        return start
                else :
                    return start -1
