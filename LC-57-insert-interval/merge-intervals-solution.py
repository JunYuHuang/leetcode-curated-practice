# O(N) T and O(N) S merge intervals solution (NeetCode's modded)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        INTERVALS_LEN = len(intervals)

        for i in range(INTERVALS_LEN):
            # `newInterval` is before `intervals[i]`
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                for j in range(i, INTERVALS_LEN):
                    res.append(intervals[j])
                return res
            # `newInterval` is after `intervals[i]`
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # `newInterval` overlaps `intervals[i]`
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res
