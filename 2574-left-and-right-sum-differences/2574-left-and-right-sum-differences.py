class Solution(object):
    def leftRightDifference(self, nums):
        left = 0
        result = []
        while left < len(nums):
            left_sum = sum(nums[:left])
            right_sum = sum(nums[left + 1:])
            result.append(abs(left_sum - right_sum))
            left += 1
        return result

               

         
         
     


         
        
        