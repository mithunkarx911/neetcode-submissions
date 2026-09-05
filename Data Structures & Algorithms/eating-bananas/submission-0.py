import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans = high
        while low<=high:
            mid=(high+low)//2
            total=sum(math.ceil(x/mid)for x in piles)
            if total<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            