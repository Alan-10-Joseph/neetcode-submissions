class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        res=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                left=mid+1
                res=mid
        return res
        









        '''
        if x==0:
            return 0
        res=1
        for i in range(1,x+1):
            if i*i>x:
                return res
            res=i
        return res
        '''