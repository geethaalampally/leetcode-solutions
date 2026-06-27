class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        out =set()
        nums.sort()
        for i in range(n):
            if (i>0) and nums[i]==nums[i-1]:
                continue
            left =i+1
            right=n-1
            while left<right:
                sumi=nums[i]+nums[left]+nums[right]
                if sumi<0:
                    left+=1
                elif sumi >0:
                    right-=1
                else:
                    triplet=tuple([nums[i], nums[left], nums[right]])
                    out.add(triplet)
                    
                    left+=1
                    right-=1
        result=[list(x) for x in out]
        return result