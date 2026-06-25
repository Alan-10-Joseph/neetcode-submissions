class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        p1=0
        nums.sort()
        res=set()
        for p1 in range(n-3):
            for p2 in range(p1+1,n-2):
                left=p2+1
                right=n-1
                while left<right:
                    total=nums[p1]+nums[p2]+nums[left]+nums[right]
                    if total==target:
                        res.add((nums[p1],nums[p2],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        ot=[list(ele) for ele in res]
        return ot
        
                


        
        