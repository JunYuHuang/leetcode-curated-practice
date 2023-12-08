# O(M + N) T and O(N) S sliding window solution (NeetCode's modded)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        INF = float("INF")
        sLen = len(s)
        need = len(t)
        have = 0
        resL = 0
        resR = INF
        l = 0
        tCount = {}
        sCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
            sCount[c] = 0
        for r in range(sLen):
            if s[r] in tCount:
                sCount[s[r]] += 1
                if sCount[s[r]] <= tCount[s[r]]:
                    have += 1
            while have == need:
                if r - l + 1 < resR - resL + 1:
                    resL = l
                    resR = r
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                l += 1
        return "" if resR == INF else s[resL:resR + 1]
