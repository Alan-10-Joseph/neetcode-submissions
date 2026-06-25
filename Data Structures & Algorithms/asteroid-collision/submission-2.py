class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for i in range(len(asteroids)):
            while stk and stk[-1]>0 and asteroids[i]<0:
                if -1*asteroids[i]==stk[-1]:
                    stk.pop()
                elif abs(asteroids[i])>stk[-1]:
                    stk.pop()
                    continue
                break
            else:
                stk.append(asteroids[i])
        return stk




















'''



        i=0
        stk=[]
        while asteroids[i]<0 and i<len(asteroids):
            stk.append(asteroids[i])
            i+=1
        if i==len(asteroids):
            return stk
        for j in range(i,len(asteroids)):
            if asteroids[j]>0:
                stk.append(asteroids[j])
            elif asteroids[j]<0:
                if abs(asteroids[j])==stk[-1]:
                    stk.pop()
                else:
                    while stk[-1]>0:
                        if abs(asteroids[j]) > stk[-1]:
                            break
                        else:
                            stk.pop()
        return stk 


        i=0
        stk=[]
        while asteroids[i]<0:
            stk.append(asteroids[i])
            i+=1
        for j in range(i,len(asteroids)):
            if stk:
                if asteroids[j]<0 and -1*asteroids[j]==stk[-1]:
                    stk.pop()
                
                    stk.append(asteroids[j])
            else:
                stk.append(asteroids[j])
        return stk
'''
        