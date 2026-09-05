from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        new=sorted(count.items(),key= lambda x:x[1],reverse=True)
        for i,j in new:
            res.append(i)
        return res[:k]        





