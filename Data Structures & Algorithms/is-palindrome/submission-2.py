class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        i=0
        j=len(s)-1
        while i <= j:

            if s[i].isalnum() and s[j].isalnum():

                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1

                else:
                    return False

            elif s[i].isalnum():
                j-=1
            
            else:
                i+=1
        return True
        '''
        cleaned=[s[i].lower() for i in range(len(s)) if s[i].isalnum()]
        return cleaned==cleaned[::-1]

        