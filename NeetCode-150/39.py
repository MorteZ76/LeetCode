class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output_list = []
        
        def findOneSeq(current, current_seq, target)  :
            if target == 0 :
                output_list.append(current_seq.copy())
                return  
            if target < 0 or current >= len(candidates) :
                return 
            current_seq.append (candidates[current])
            findOneSeq(current, current_seq, target - candidates[current]) 
            current_seq.pop() 
            findOneSeq(current + 1, current_seq, target)

        findOneSeq(0, [], target)
        return output_list 


        
        