# O(N) T and O(1) S greedy solution (NeetCode's modded)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        S_SIZE = len(s)
        res = []
        lastPos = {} # maps char to its count in `s`
        l = 0
        r = 0

        # build the `lastPos` hashmap
        for i in range(S_SIZE):
            lastPos[s[i]] = i

        for i in range(S_SIZE):
            if lastPos[s[i]] > r:
                r = lastPos[s[i]]

            # reached end of a substring
            if i == r:
                # add its size to `res`
                res.append(r - l  + 1)

                # exit loop if substring is last one
                if r == S_SIZE - 1:
                    break

                # update pointers for next substring
                l = r + 1
                r = l

        return res