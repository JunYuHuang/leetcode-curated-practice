# O(26 * N) T and O(1) S sliding window solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        if s2Len < s1Len: return False

        s3 = s1 + s2
        s1Count = { c : 0 for c in s3 }
        s2Count = { c : 0 for c in s3 }
        for c in s1:
            s1Count[c] += 1
        l = 0
        r = 0
        while r < s2Len:
            s2Count[s2[r]] += 1
            windowSize = r - l + 1
            if windowSize == s1Len:
                if s2Count == s1Count:
                    return True
                s2Count[s2[l]] -= 1
                l += 1
            r += 1
        return False
