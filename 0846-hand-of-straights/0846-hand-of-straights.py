class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()
        
        h = []
        
        for card in hand:
            if len(h) == 0:
                heapq.heappush(h, (card, 1))
                continue
            
            _min, count = heapq.heappop(h)
            
            if _min + 1 != card:
                heapq.heappush(h, (_min, count))
                heapq.heappush(h, (card, 1))
                continue
            
            if count + 1 > groupSize:
                heapq.heappush(h, (card, 1))
                continue
            
            if count + 1 == groupSize:
                continue
            heapq.heappush(h, (card, count + 1))
        print(h)
        for card, count in h:
            if count < groupSize:
                return False
        return True
        