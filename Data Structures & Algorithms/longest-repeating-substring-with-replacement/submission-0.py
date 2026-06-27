class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxFreq=0
        n=len(s)
        ans=0
        count={}
        for r in range(n):
            count[s[r]]=count.get(s[r],0)+1
            maxFreq=max(maxFreq,count[s[r]])
            if (r-l+1)-maxFreq>k:
                count[s[l]]-=1
                l+=1
            currWindow=r-l+1
            ans=max(currWindow,ans)
        return ans
            


    
        