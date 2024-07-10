# O(N) T and O(N) S greedy solution (NeetCode's modded)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        TRIPLETS_SIZE = len(triplets)
        matchedIndices = set()

        for trip in triplets:
            # skip invalid triplets
            if (trip[0] > target[0] or
                trip[1] > target[1] or
                trip[2] > target[2]):
                continue

            # mark valid positions from `trip`
            for i in range(3):
                if trip[i] == target[i]:
                    matchedIndices.add(i)

        return len(matchedIndices) == 3