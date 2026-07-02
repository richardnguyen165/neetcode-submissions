import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        global_max = global_min = 1

        for num in nums:
            if num == 0:
                global_max = global_min = 1
                continue
            # So that curMin can use the old max, not the new max
            tmp = num * global_max
            # (Postive * Postive, Negative * Negative, Number itself (could be greater))
            global_max = max(global_max * num, global_min * num, num)
            global_min = min(tmp, global_min * num, num)

            # CurMax, CurMin -> current segment until either till the end or zero

            # Update global maximum
            res = max(res, global_max)
        return res
            

