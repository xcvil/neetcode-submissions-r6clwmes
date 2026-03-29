class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        avgK = math.ceil(sum(piles)/h)
        m = max(piles)

        minK = m
        l, r = 1, m
        while l <= r:
            m = l + ((r-l)//2)
            asHour = sum(math.ceil(pile/m) for pile in piles)
            if asHour > h:
                l = m + 1
            else:
                r = m - 1
                minK = min(minK, m)
        return minK
            
                

