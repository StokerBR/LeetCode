class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        sorted_keys = sorted(count.keys())

        for k in sorted_keys:
            if count[k] > 0:
                start_count = count[k]
                for i in range(k, k + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count

        return True
