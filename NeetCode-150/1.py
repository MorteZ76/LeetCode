
class Solution:
    def twoSum(self, nums: List[int], target: int) ->   List[int]:
        val_to_index = {}
        for i, n in enumerate (nums): 

            if (target - n) in val_to_index :
                return [val_to_index[target - n], i]
            else :
                val_to_index[n] = i
            
                

        