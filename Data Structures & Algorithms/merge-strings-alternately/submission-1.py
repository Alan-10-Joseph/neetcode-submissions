class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        j=0
        ot=""

        while i<l1 and  j<l2:
            ot+=word1[i]
            ot+=word2[j]
            i+=1
            j+=1

        while i<l1:
            ot+=word1[i]
            i+=1

        while j<l2:
            ot+=word2[j]
            j+=1

        return ot
        