class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ot=[]
        for i in range(n):
            pd=1
            for j in range(n):
                if i!=j:
                    pd*=nums[j]
            ot.append(pd)
        return ot