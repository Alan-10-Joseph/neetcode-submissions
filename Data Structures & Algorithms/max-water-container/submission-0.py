class Solution:
    def maxArea(self, heights: List[int]) -> int:
     
        n=len(heights)
        left=0
        right=n-1
        maxVol=0
        while left<right:
            height=min(heights[left],heights[right])
            vol=(right-left)*height
            maxVol=max(vol,maxVol)
            if height==heights[left] and height==heights[right]:
                left+=1
                right-=1
            elif height==heights[left]:
                left+=1
            else:
                right-=1
        return maxVol




        