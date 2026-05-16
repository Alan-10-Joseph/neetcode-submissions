class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        """
        nums.sort()
        n=len(nums)//2
        return nums[n]
        
        from collections import Counter

        freq = Counter(nums)
        max_ele = max(list(freq.values()))
        for ele in freq:
            if freq[ele] == max_ele:
                return ele
        """
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate