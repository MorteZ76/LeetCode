class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        best_cost = []
        best_cost.append(0)
        best_cost.append(0)
        i = 2
        while i < len(cost) + 1:
            best_cost.append(min(best_cost[i-1] + cost[i-1], best_cost[i-2] + cost[i-2]))
            i += 1
        return best_cost[-1]
        