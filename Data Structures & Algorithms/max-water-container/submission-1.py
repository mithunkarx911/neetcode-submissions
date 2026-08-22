class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        left,right=0,len(heights)-1
        while left < right:
            l=right-left
            b=min(heights[left],heights[right])
            a=l*b
            maxi=max(maxi,a)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1    
                
        return maxi    
        