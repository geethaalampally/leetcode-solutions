class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx=-1
        if needle in haystack:
            idx=haystack.index(needle)
        return idx
        