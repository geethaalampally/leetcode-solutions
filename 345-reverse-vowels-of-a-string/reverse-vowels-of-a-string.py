class Solution:
    def reverseVowels(self, s: str) -> str:
        li = list(s)
        vowels = "aeiouAEIOU"

        i = 0
        j = len(s) - 1

        while i < j:
            if li[i] not in vowels:
                i += 1
            elif li[j] not in vowels:
                j -= 1
            else:
                li[i], li[j] = li[j], li[i]
                i += 1
                j -= 1

        return "".join(li)