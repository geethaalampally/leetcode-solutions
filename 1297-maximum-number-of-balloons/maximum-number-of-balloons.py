class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}

        for char in text:
            if char not in freq and char in "balon":
                freq[char] = 1
            elif char in freq:
                freq[char] += 1

        if len(freq) < 5:
            return 0

        freq['l'] //= 2
        freq['o'] //= 2

        return min(freq.values())