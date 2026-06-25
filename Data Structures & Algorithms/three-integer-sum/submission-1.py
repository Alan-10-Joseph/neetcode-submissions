class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for pointer in range(n-2):
            left=pointer+1
            right=n-1
            while left<right:
                total=nums[pointer]+nums[left]+nums[right]
                if total==0:
                    val=[nums[pointer],nums[left],nums[right]]
                    if val not in res:
                        res.append(val)
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return res
                








        '''
        n=len(nums)
        ot=[]
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        ot.append([nums[i],nums[j],nums[k]])
        return ot
        '''