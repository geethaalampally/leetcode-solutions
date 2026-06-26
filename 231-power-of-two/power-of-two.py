class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=1
        while True:
            if i>=n:
                break
            i*=2
        return i==n
        
        