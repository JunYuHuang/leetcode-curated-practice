# O(N) T and O(1) S greedy solution (NeetCode's modded)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        SIZE = len(gas)
        tank = 0
        pos = 0

        for i in range(SIZE):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                pos = i + 1

        return pos