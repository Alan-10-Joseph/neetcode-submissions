class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ot=""
        for f,l in zip(first,last):
            if f==l:
                ot+=f
            else:
                return ot
        return ot        