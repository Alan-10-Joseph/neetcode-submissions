class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        l=0
        r=0
        n=len(nums)
        while r<n:
            if (r-l)>k:
                seen.remove(nums[l])
                l+=1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r+=1
        return False
            



        '''
        seen={}
        n=len(nums)
        for p2 in range(n):
            if nums[p2] not in seen:
                seen[nums[p2]]=p2
            else:
                if abs(seen[nums[p2]]-p2)<=k:
                    return True
                else:
                    seen[nums[p2]]=p2
        return False
        


'''






        '''
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    if abs(j-i)<=k:
                        return True
                        break
                else:
                    continue
        return False
        '''