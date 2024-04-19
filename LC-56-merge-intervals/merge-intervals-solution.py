# O(NLogN) T and O(N) S merge intervals solution (NeetCode's modded)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        INTERVALS_LEN = len(intervals)

        for i in range(1, INTERVALS_LEN):
            # no overlap
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            # they overlap
            else:
                # merge them
                res[-1][1] = max(
                    res[-1][1], intervals[i][1]
                )
        return res
