class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Length index is the actual thing we want to find
        cost_array = [0] * (len(cost) + 1)

        # Starting at index 0 and index 1 would be cost 0

        for i in range(2, len(cost_array)):
            cost_array[i] = min(cost_array[i - 1] + cost[i - 1], cost_array[i - 2] + cost[i - 2])

        return cost_array[-1]