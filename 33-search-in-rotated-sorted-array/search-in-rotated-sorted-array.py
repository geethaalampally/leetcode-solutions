class Solution:

    def bin_search(self, left, right, nums, target):

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:

        # Find the pivot (smallest element)
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Pivot is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1

            # Pivot is in the left half (including mid)
            else:
                right = mid

        pivot = left

        # Decide which sorted half to search
        if nums[pivot] <= target <= nums[-1]:
            return self.bin_search(
                pivot,
                len(nums) - 1,
                nums,
                target
            )

        return self.bin_search(
            0,
            pivot - 1,
            nums,
            target
        )