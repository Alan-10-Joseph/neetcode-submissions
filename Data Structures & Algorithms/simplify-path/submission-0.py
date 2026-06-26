class Solution:
    def simplifyPath(self, path: str) -> str:
        stk=[]
        for directory in path.split("/"):
            if directory == "" or directory==".":
                continue
            elif directory=="..":
                if stk:
                    stk.pop()
            else:
                stk.append(directory)
        return "/"+"/".join(stk)