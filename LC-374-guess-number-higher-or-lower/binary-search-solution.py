# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# O(LogN) T and O(1) S binary search solution
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            m = l + (r - l) // 2
            myGuess = guess(m)
            if myGuess == 0:
                return m
            elif myGuess == -1:
                r = m - 1
            else: # myGuess == 1
                l = m + 1
