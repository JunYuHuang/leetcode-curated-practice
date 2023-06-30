# O(Log(max(P)) * P) T and O(1) S binary search solution where P = piles (NeetCode's modded)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftK = 1
        rightK = max(piles)
        k = rightK

        while leftK <= rightK:
            midK = (leftK + rightK) // 2

            # calc the time (in hours) needed to finish piles at speed `midK`
            time = 0
            for p in piles:
                timeToFinish = math.ceil(p / midK)
                time += timeToFinish

            if time <= h:
                # update k if speed `midK` is slower than it
                if midK < k: k = midK
                # too fast or just right, try slower `midK` speed next loop
                rightK = midK - 1
            else: # time > h
                # too slow, try faster `midK` speed next loop
                leftK = midK + 1
        return k
