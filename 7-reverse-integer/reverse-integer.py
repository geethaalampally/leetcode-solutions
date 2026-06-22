class Solution:
    def reverse(self, x: int) -> int:
        # sign = -1 if x < 0 else 1
        # num = abs(x)
        # rev = int(str(num)[::-1])
        # rev *= sign
        # if rev < -(2**31) or rev > (2**31 - 1):
        #     return 0
        # return rev

        sign = -1 if x < 0 else 1

        num = abs(x)
        res = 0

        while num > 0:
            rem = num % 10
            res = res * 10 + rem
            num = num // 10

        res = res * sign

        if res < -(2**31) or res > (2**31 - 1):
            return 0

        return res

