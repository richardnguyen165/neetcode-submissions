class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        elif len(cost) == 3:
            return min(cost[1], cost[0] + cost[2])

        all_costs = [0 for _ in range(len(cost) + 1)]
        for index in range(2, len(cost) + 1):
            all_costs[index] = min(all_costs[index - 1] + cost[index - 1], all_costs[index - 2] + cost[index - 2])
        return all_costs[len(cost)]
        