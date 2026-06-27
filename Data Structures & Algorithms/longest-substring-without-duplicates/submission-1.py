class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        seen=set()
        l=0
        n=len(s)
        maxLength=1
        for r in range(n):
            if s[r] not in seen:
                seen.add(s[r])
                length=r-l+1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            maxLength=max(length,maxLength)
        return maxLength

        