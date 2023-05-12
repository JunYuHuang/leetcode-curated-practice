# O(N) T and O(N) S bucket sort solution (NeetCode's modded)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        valToCount = {}
        maxCount = 1
        for n in nums:
            valToCount[n] = valToCount.get(n, 0) + 1
            if valToCount[n] > maxCount:
                maxCount = valToCount[n]
        countToVal = [None] * (1 + maxCount)
        for i in range(len(countToVal)):
            countToVal[i] = []
        for n in valToCount:
            countToVal[valToCount[n]].append(n)
        for i in range(maxCount, 0, -1):
            if len(res) == k: break
            for n in countToVal[i]:
                if len(res) == k: break
                res.append(n)
        return res
