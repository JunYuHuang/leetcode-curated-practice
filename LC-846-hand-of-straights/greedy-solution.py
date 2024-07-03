# O(NLogN) T and O(N) S greedy solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                nextCard = card + i
                if nextCard not in count:
                    return False
                if count[nextCard] == 0:
                    return False

                count[nextCard] -= 1
                if count[nextCard] < 0:
                    return False
        return True