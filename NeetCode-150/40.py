class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output_list = []
        candidates.sort()
        def findOneSeq(current, current_seq, target)  :
            if target == 0 :
                output_list.append(current_seq.copy())
                return  
            if target < 0 or current >= len(candidates) :
                return 
            next_current = current 
            new_target = target
            while next_current < len(candidates) and candidates[next_current] == candidates[current]  :
                next_current += 1
            
            while current < next_current : 
                current_seq.append (candidates[current])
                new_target = new_target- candidates[current]
                findOneSeq(next_current, current_seq, new_target) 
                current += 1
            while current_seq and current_seq[-1] == candidates[current-1] :
                current_seq.pop() 
            findOneSeq(next_current, current_seq, target)
        findOneSeq(0, [], target)
        return list(output_list) 


        
        