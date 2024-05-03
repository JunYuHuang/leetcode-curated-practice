# O(NLogN) T and O(N) intervals solution (NeetCode's modded)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        INTERVALS_LEN = len(intervals)
        res = 0
        count = 0
        s = 0
        e = 0
        starts = []
        ends = []

        for intv in intervals:
            starts.append(intv[0])
            ends.append(intv[1])

        starts.sort()
        ends.sort()

        while s < INTERVALS_LEN:
            # meeting started before another ended
            # or overlap
            if starts[s] < ends[e]:
                count += 1
                if count > res:
                    res = count
                s += 1
            # meeting ended or no overlap
            else:
                count -= 1
                e += 1
        return res
