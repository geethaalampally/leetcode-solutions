class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # val1=0
        # val2=0
        # for char in s:
        #     val1+=ord(char)
        # for char in t:
        #     val2+=ord(char)
        # diff=val2-val1
        # return chr(diff)

        # for char in t:
        #     if s.count(char)!=t.count(char):
        #         return char

        xor = 0

        for ch in s:
            xor ^= ord(ch)

        for ch in t:
            xor ^= ord(ch)

        return chr(xor)
        