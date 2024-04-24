# O(NLogN) T and O(1) S merge intervals solution (NeetCode's modded)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]
        INTERVALS_LEN = len(intervals)

        for i in range(1, INTERVALS_LEN):
            # there is overlap
            if intervals[i][0] < lastEnd:
                # keep the interval that ends sooner
                lastEnd = min(
                    lastEnd, intervals[i][1]
                )
                res += 1
            # there is NO overlap
            else:
                lastEnd = intervals[i][1]

        return res
