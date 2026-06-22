class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        seen=set()
        right=0
        left=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            count=max(count,len(seen))
        return count