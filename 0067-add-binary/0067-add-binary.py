class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        result = ""
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                digit_a = int(a[i])
                i -= 1
            else:
                digit_a = 0
            if j >= 0:
                digit_b = int(b[j])
                j -= 1
            else:
                digit_b = 0
            total = digit_a + digit_b + carry
            result = str(total % 2) + result
            carry = total // 2
        return result