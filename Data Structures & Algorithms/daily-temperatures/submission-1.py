class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        n=len(temperatures)
        res=[0]*n
        stk.append((temperatures[-1],n-1))
        r=n-2
        while r>=0:
            while stk:
                if temperatures[r]<stk[-1][0]:
                    res[r]=stk[-1][1]-r
                    stk.append((temperatures[r],r))
                    break
                else:
                    stk.pop()
            else:
                stk.append((temperatures[r],r))
            r-=1
        return res

                





        '''
        n=len(temperatures)
        res=[0]*n
        for i in range(n-1):
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    res[i]=j-i
                    break
                else:
                    continue
        return res
        '''