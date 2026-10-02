class Solution:
    def longestCommonPrefix(self,strs):
        reference_word=strs[0]
        #This loop is going to loop from zero to the length of the reference word
        for character_index in range(len(reference_word)):
            current_character=reference_word[character_index]
            
            #looping through each word in the array
            
            for str in strs:
                
                if character_index >= len(str):
                    return reference_word[:character_index]
                if str[character_index] != current_character:
                    return reference_word[:character_index]
                
        return reference_word
strs = ["flower","flow","flight"]   
sol_instance=Solution()
print(sol_instance.longestCommonPrefix(strs))