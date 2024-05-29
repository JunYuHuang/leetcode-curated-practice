# O(N) T and O(1) S sliding window (NeetCode's modded)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ARR_LEN = len(arr)
        res = 1
        l = 0
        prevSign = "="

        for r in range(1, ARR_LEN):
            # is turbulent
            if (
                prevSign != "<" and
                arr[r - 1] < arr[r]
            ):
                res = max(res, r - l + 1)
                prevSign = "<"
            # is turbulent
            elif (
                prevSign != ">" and
                arr[r - 1] > arr[r]
            ):
                res = max(res, r - l + 1)
                prevSign = ">"
            # is not turbulent
            elif arr[r - 1] == arr[r]:
                l = r
                prevSign = "="
            # is not turbulent
            else:
                l = r - 1
                isLesser = arr[r - 1] < arr[r]
                prevSign = "<" if isLesser else ">"

        return res
