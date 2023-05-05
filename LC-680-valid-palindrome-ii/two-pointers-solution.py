# O(N) T and O(1) S two pointers solution (NeetCode's modded)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPali(s): return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1:r + 1]
                skipR = s[l:r]
                return (self.isPali(skipL) or
                        self.isPali(skipR))
            l, r = l + 1, r - 1
        return True

    def isPali(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l, r = l + 1, r - 1
        return True
