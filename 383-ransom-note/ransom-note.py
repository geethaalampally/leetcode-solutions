class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        c1=Counter(ransomNote)
        c2=Counter(magazine)

        for char in c1:
            if char not in c2 or c1[char]>c2[char]:
                return False
        return True

        