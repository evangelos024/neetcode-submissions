class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        rs = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                a+=s[i]

        a = a.lower()           
        for i in range(len(a)-1,-1,-1):
            rs+=a[i]
      
        if rs == a:
            return(True)
        else:
            return(False)
