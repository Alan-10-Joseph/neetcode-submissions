class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=set(nums)
        maxCount=0
        for num in nums:
            if num-1 not in m:
                count=0
                while num in m:
                    count+=1
                    num=num+1
            else:
                continue
            maxCount=max(maxCount,count)
        return maxCount
