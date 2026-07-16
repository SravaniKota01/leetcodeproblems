class Solution(object):
    def pivotIndex(self, nums):
     left = 0
     while left < len(nums):
      left_sum = sum(nums[:left])
      right_sum = sum(nums[left + 1:])
      if left_sum == right_sum:
        return left
        break
      else:
         left += 1
     else:
      return -1

            
        