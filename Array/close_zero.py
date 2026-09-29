# given an array of integer array of nums of size n, return the value closest to 0 in the  nums.if there are multiple numbers return the number with the largest value

class Solution:
    def findClosestNumber(self, nums):
        closest=nums[0]
        
        for num in nums:
            if abs(num) < abs(closest):
                closest=num
            elif abs(num) == abs(closest):
                if num > closest:
                    closest=num
                    
        return closest
nums=[-1,1,2,3,4,5,6]   
sol_instance=Solution()
print(sol_instance.findClosestNumber(nums))