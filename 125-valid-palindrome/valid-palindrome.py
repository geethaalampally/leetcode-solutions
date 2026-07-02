class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        for char in s:
            if char.isalnum():
                t.append(char.lower())
        t="".join(t)
        val=1
        if len(t)==0:
            val=1
        i=0
        j=len(t)-1
        while i<j:
            if t[i]!=t[j]:
                val=0
                break
            i+=1
            j-=1
        return bool(val)
        