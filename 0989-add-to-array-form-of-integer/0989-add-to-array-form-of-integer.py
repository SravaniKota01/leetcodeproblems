class Solution(object):
    def addToArrayForm(self, num, k):
        temp = 0
        for i in num:
            temp = temp *10 + i
        total = 0
        total = temp + k
        result = []
        for i in str(total):
            result.append(int(i))
        return result
        