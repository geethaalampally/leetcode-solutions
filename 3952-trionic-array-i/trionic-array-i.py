class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        # increasing
        while i < n and nums[i] > nums[i-1]:
            i += 1

        if i == 1 or i == n:
            return False

        # decreasing
        while i < n and nums[i] < nums[i-1]:
            i += 1

        if i == n:
            return False

        # increasing again
        while i < n and nums[i] > nums[i-1]:
            i += 1

        return i == n