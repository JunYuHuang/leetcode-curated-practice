# O(NLogN) T and O(1) S merge intervals solution
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        INTERVALS_LEN = len(intervals)
        intervals.sort()

        for i in range(1, INTERVALS_LEN):
            lastEnd = intervals[i - 1][1]
            currStart = intervals[i][0]

            # no overlap
            if lastEnd <= currStart:
                continue

            # they overlap
            return False

        return True
