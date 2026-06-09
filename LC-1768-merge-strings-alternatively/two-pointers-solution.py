# My 2-pointers O(m + n) T + O(m + n) S solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Len = len(word1)
        word2Len = len(word2)
        l = 0
        r = 0
        res = []
        isWord1 = True

        while l < word1Len and r < word2Len:
            if isWord1:
                res.append(word1[l])
                l += 1
            else:
                res.append(word2[r])
                r += 1
            isWord1 = not isWord1

        while l < word1Len:
            res.append(word1[l])
            l += 1

        while r < word2Len:
            res.append(word2[r])
            r += 1

        return "".join(res)