class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for el in s:

            if el in "({[":
                stk.append(el)

            else:
                if not stk:
                    return False
                
                top=stk.pop(-1)
                if el == ")" and top != "(":
                    return False
                elif el =="]" and top != "[":
                    return False
                elif el =="}" and top !="{":
                    return False
            
        return len(stk)==0
                
                