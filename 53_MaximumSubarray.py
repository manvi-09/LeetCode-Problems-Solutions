#Name : Manvi Goyal
#Date : 04/10/2022

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)
        if result<=0:
            return result
        
        sum = 0
        for i in nums:
            sum = max(sum+i,0)  #Updating the value of sum variable in each iteration
            result=max(sum,result)  #For finding maximum out of sum and result
                
        return result
