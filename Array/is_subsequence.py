class Solution:
    def isSubsequence(self, s,t):
        character_order=""
        i,j=0,0
        
        while i < len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
            
        return i==len(s)

s = "abc"
t = "ahbgdc"   
sol_instance=Solution()
print(sol_instance.isSubsequence(s,t))