from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        freq=[[] for _ in range(0,len(nums)+1)]
        for num,counti in count.items():
            freq[counti].append(num)
        res=[]    
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res



