class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anag={}
        for str in strs:
            main_anag=" ".join(sorted(str))
            if main_anag in group_anag:
                group_anag[main_anag].append(str)
            else:
                group_anag[main_anag]=[str]
        return list(group_anag.values())


        