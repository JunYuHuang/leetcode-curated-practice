# O(N + KLogN) T and O(N) S max heap solution
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxH = [-1 * n for n in nums]
        heapq.heapify(maxH)
        for _ in range(k - 1):
            heapq.heappop(maxH)
        return -1 * maxH[0]