class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lenS1=len(s1)
        freqs1=[0]*26
        lenS2=len(s2)
        l=0
        if lenS2<lenS1:
            return False
        freqs2=[0]*26
        for r in range(lenS1):
            freqs1[ord(s1[r])-ord("a")]+=1
            freqs2[ord(s2[r])-ord("a")]+=1
        if freqs1==freqs2:
                return True
        r+=1
        while r<lenS2:
            freqs2[ord(s2[l])-ord("a")]-=1
            freqs2[ord(s2[r])-ord("a")]+=1
            if freqs1==freqs2:
                return True
            r+=1
            l+=1
            
        return False



