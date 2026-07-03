class Solution(object):
    def alternateDigitSum(self, n):
        sign = 1
        total = 0

        for digit in str(n):
            total += sign * int(digit)
            sign *= -1

        return total