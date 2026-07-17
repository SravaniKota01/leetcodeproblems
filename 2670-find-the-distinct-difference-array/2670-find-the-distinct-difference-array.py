class Solution(object):
    def distinctDifferenceArray(self, nums):
        left = 0
        result = []
        while left < len(nums):
            num1 = nums[:left + 1]
            num2 = nums[left + 1:]
            count = 0
            stack = []
            for i in num1:
                if i not in stack:
                    stack.append(i)
                    count += 1
            count1 = 0
            stack1 = []
            for i in num2:
                if i not in stack1:
                    stack1.append(i)
                    count1 += 1
            result.append(count - count1)
            left += 1
        return result

        