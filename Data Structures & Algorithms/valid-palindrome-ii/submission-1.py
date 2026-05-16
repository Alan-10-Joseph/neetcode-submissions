class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        i=0
        j=len(s)-1
        count=1
        while i<j:
            if count==0 and s[i]!=s[j]:
                return False
            elif count==1 and s[i]!=s[j]:
                count=0
                i+=1
                j-=1
            else:
                i+=1
                j-=1
        return True

        '''

        def palindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True


        left=0
        right=len(s)-1
        while left < right:
            if s[left]!=s[right]:
                return palindrome(left+1,right) or palindrome(left,right-1)
            left+=1
            right-=1
        return True
            
            