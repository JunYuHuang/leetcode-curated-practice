# O(KLogN) T and O(N) S max heap solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        valToCount = {}
        for n in nums:
            valToCount[n] = valToCount.get(n, 0) + 1
        maxH = [(-valToCount[n], n) for n in valToCount]
        heapq.heapify(maxH)
        for i in range(k):
            count, n = heapq.heappop(maxH)
            res.append(n)
        return res
