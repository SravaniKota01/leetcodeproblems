class Solution(object):
    def myAtoi(self, s):
        s = s.strip()      
        if s == "":
            return 0
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        result = ""
        for ch in s:
            if ch.isdigit():
                result += ch
            else:
                break
        if result == "":
            return 0
        result = sign * int(result)
        if result < -2**31:
            return -2**31

        if result > 2**31 - 1:
            return 2**31 - 1
        return result