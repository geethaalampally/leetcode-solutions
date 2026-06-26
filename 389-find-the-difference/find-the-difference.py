class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        val1=0
        val2=0
        for char in s:
            val1+=ord(char)
        for char in t:
            val2+=ord(char)
        diff=val2-val1
        return chr(diff)

        
        