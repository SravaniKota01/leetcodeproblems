class Solution(object):
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        l = []
        elementin_l = 0
        for num in nums:
            elementin_l = max(elementin_l, num)
            l.append(gcd(num, elementin_l))
        l.sort()
        left = 0
        right = len(l) - 1
        ans = 0
        while left < right:
            ans += gcd(l[left], l[right])
            left += 1
            right -= 1
        return ans
        