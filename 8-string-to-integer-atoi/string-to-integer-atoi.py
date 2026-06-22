class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Empty string after removing spaces
        if i == n:
            return 0

        sign = 1

        # Check sign
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        res = 0

        # Read digits
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign

        # Clamp to 32-bit signed integer range
        if res < -(2**31):
            return -(2**31)

        if res > (2**31 - 1):
            return 2**31 - 1

        return res