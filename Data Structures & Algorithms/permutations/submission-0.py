class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def all_perms(current_comb, index_list):
            results= []

            if len(current_comb) == len(nums):
                results.append(current_comb)
                return results

            for index in range(0, len(nums)):
                if index not in index_list:
                    copy_of_index_list = index_list[:]
                    copy_of_index_list.append(index)

                    copy_of_current_comb = current_comb[:]
                    copy_of_current_comb.append(nums[index])

                    results.extend(all_perms(copy_of_current_comb, copy_of_index_list))
            return results

        return all_perms([], [])