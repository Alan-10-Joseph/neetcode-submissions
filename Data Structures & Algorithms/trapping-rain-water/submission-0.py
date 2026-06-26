class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        leftMax=height[0]
        rightMax=height[-1]
        i=0
        while i<n:
            j=-i-1
            leftMax=max(leftMax,height[i])
            rightMax=max(rightMax,height[j])
            left[i]=leftMax
            right[j]=rightMax
            i+=1
        vol=0
        for j in range(n):
            vol+=max(min(left[j],right[j])-height[j],0)
        return vol


        