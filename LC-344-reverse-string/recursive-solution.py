# My O(N) time and O(N) space recursive solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recurse(l, r):
            if l > r: return
            if s[l] != s[r]: s[l], s[r] = s[r], s[l]
            recurse(l + 1, r - 1)
        recurse(0, len(s) - 1)