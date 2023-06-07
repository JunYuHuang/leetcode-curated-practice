# O(N) T and O(1) S two pointers solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def isAlphaNum(self, c):
        return '0' <= c <= '9' or 'a' <= c.lower() <= 'z'
