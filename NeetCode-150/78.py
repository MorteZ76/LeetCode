class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        final_output = []
        def make_new_lists(nums) :
            if len(nums) == 1 :
                return [[nums[0]], []]
            output = make_new_lists(nums[1:]) 
            n = len(output)
            for i in range(n):
                if output[i] == [] :
                    new_list = [nums[0]]
                else :
                    new_list = output[i].copy()
                    new_list.append(nums[0])

                output.append(new_list)
            return output
        final_output.extend(make_new_lists(nums))
        return final_output
