class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0

        for i in range(len(nums)):

            # Current position is unreachable
            if i > max_idx:
                return False

            # Update farthest reachable index
            max_idx = max(max_idx, i + nums[i])

            # Already can reach the end
            if max_idx >= len(nums) - 1:
                return True

        return True