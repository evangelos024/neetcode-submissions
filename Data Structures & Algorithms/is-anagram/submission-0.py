class Solution:
    def isAnagram(self,s,t):
        a = list(s)
        b = list(t)
        
        if(sorted(a) == sorted(b)):
            return(True)
        return(False)
                

        