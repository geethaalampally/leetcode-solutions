class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # dict={}
        # for i in range(len(nums)):
        #     if nums[i] not in dict:
        #         dict[nums[i]]=i
        #     else:
        #         diff=i-dict[nums[i]]
        #         if diff<=k:
        #             return True
        #         else:
        #             dict[nums[i]]=i
        # return False

        seen={}
        for i , num in enumerate(nums):
            if num in seen and i-seen[num]<=k:
                return True
            seen[num]=i
        return False
                    