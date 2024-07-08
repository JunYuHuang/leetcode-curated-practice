# O(N) T and O(N) S greedy solution (NeetCode's expl.)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        TRIPLETS_SIZE = len(triplets)
        invalidIndices = set()
        matchedIndices = set()

        # mark invalid triplets' indices
        for i in range(TRIPLETS_SIZE):
            for j in range(3):
                if triplets[i][j] > target[j]:
                    invalidIndices.add(i)
                    break

        for i in range(TRIPLETS_SIZE):
            # skip invalid triplets
            if i in invalidIndices:
                continue

            # mark matched indices in target
            for j in range(3):
                if triplets[i][j] == target[j]:
                    matchedIndices.add(j)

        return len(matchedIndices) == 3