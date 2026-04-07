class Solution: 
    def searchSpeed(self, l: int, r: int, piles: List[int], h:int):

        if l > r:
            return l
        total = 0
        mid = l + (r - l) //2

        for pile in piles:
            total += math.ceil(pile/mid)
        if total <= h:
            return self.searchSpeed(l,mid-1,piles,h)
        else:
            return self.searchSpeed(mid + 1, r, piles, h)



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.searchSpeed(1, max(piles), piles, h)

        