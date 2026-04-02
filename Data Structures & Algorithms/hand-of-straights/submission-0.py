class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1
        
        sortedKeys = sorted(count.keys())

        j = 0
        while j < len(sortedKeys):
            num = sortedKeys[j]
            if count[num] > 0:
                for i in range(num, num + groupSize):
                    if i not in count or count[i] <= 0:
                        return False
                    count[i] -= 1
            else:
                j += 1
        return True