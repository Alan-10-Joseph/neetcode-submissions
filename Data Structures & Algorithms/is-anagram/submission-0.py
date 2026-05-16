class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord("a")]+=1
        for ch in t:
            freq[ord(ch)-ord("a")]-=1
        if sum([abs(fre) for fre in freq])==0:
            return True
        else:
            return False

        