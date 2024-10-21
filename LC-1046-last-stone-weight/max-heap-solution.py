# O(NLogN) T and O(N) S solution (NeetCode's modded)
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            if stone1 == stone2:
                continue

            newStone = abs(stone1 - stone2) * -1
            heapq.heappush(maxHeap, newStone)

        if len(maxHeap) == 0:
            return 0
        else:
            return maxHeap[0] * -1
