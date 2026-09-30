class Solution:
    def mergeAlternately(self, word1, word2):
        combined_string=""
        word1_stack=list(word1[::-1])
        word2_stack=list(word2[::-1])
        
        while word1_stack:
            combined_string+=word1_stack.pop()
            
            if word2_stack:
                combined_string+=word2_stack.pop()
                
        while word2_stack:
            combined_string+=word2_stack.pop()
            
        return combined_string
    
word1="abc"  
word2="pqrs"
sol_instance=Solution()
print(sol_instance.mergeAlternately(word1, word2))