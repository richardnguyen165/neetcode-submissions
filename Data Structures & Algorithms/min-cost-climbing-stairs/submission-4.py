class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # This is a problem where we DO NOT NEED TO END AT THE LAST STEP (JUST PAST IT)*****
        # But we need to end at the previous case -> change the return case

        # In this case, we get either take the result of the previous step, or previous 2 steps
        
        all_results = [0 for _ in range(len(cost) + 1)]

        for index in range(2, len(cost) + 1):
            all_results[index] = min(all_results[index - 2] + cost[index - 2], all_results[index - 1] + cost[index - 1])
        
        return all_results[len(cost)]

