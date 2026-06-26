class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        ot=[]
        for ele in freq:
            if freq[ele]>(len(nums)/3):
                ot.append(ele)
        return ot
        