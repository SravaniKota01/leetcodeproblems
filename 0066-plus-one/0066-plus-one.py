class Solution(object):
    def plusOne(self, digits):
        num = 0
        for d in digits:
            num = num * 10 + d
        temp = num + 1
        result = []
        for i in str(temp):
            result.append(int(i))
        return result
        
                           
        