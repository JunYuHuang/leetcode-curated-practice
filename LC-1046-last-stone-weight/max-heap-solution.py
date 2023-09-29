# O(NLogN) T and O(N) S max heap solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            stoneX = -1 * heapq.heappop(maxHeap)
            stoneY = -1 * heapq.heappop(maxHeap)
            if stoneX == stoneY: continue
            newStone = -1 * abs(stoneX - stoneY)
            heapq.heappush(maxHeap, newStone)

        return maxHeap[0] * -1 if maxHeap else 0
