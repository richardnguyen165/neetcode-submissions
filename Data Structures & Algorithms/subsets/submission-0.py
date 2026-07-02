class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def sub_gen(length_of_nums = 0, current_comb = [], index_chosen = -1):
            if index_chosen == length_of_nums:
                return []

            all_combs = []

            if index_chosen == -1:
                all_combs.append([])
                
            for index, number in enumerate(nums):
                if index > index_chosen:
                    copy_current_comb = current_comb[:]
                    copy_current_comb.append(number)
                    all_combs.append(copy_current_comb)
                    all_combs.extend(sub_gen(length_of_nums + 1, copy_current_comb, index))
            
            return all_combs

        result = sub_gen(len(nums) - 1)
        return result