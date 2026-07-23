class Solution:
    def isAnagram(self,s,t):
        if(sorted(list(s)) == sorted(list(t))):
            return(True)
        return(False)