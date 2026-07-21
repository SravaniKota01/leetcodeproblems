class Solution(object):
    def hasAlternatingBits(self, n):
        list = []
        while n!= 0:
            digit = n%2
            list.append(digit)
            n = n//2
        for i in range(1,len(list)):
            if(list[i-1] == list[i]):
                return False
        return True

        