class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        res = 0

        while x > 0:
            rem = x % 10
            res = res * 10 + rem
            x = x // 10

        if res == temp:
            return True
        else:
            return False
        