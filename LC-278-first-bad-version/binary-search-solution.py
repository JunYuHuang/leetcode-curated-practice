# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# O(LogN) T and O(1) S binary search solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return n
        l = 0
        r = n
        while True:
            m = l + (r - l) // 2
            mRes = isBadVersion(m)
            if mRes and not isBadVersion(m - 1):
                return m
            elif mRes:
                r = m - 1   # search left half
            else: # !mRes
                l = m + 1   # search right half
