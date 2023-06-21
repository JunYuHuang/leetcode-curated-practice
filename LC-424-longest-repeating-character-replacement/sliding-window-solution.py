# O(N) T and O(N) S sliding window solution (NeetCode's modded)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = r = maxCount = 0
        count = { c : 0 for c in s }
        N = len(s)
        while r < N:
            count[s[r]] += 1
            maxCount = max(maxCount, count[s[r]])
            while r - l + 1 - maxCount > k: # ran out of replacement chars
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
