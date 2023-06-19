# O(N) T and O(N) S sliding window solution (NeetCode's expl.)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N <= 1: return N

        res = l = r = 0
        seen = set()
        while r < N:
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            windowSize = r - l + 1
            if windowSize > res:
                res = windowSize
            r += 1
        return res
