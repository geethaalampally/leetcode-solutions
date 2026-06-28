class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        pivot=-1
        if sum(nums[1:])==0:
            pivot= 0
        # elif sum(nums[:n-1])==nums[-1]:
        #     pivot= -1
        else:
            sum1=sum2=0
            for i in range(1,n):
                sum1=sum(nums[:i])
                sum2=sum(nums[i+1:])
                if sum1==sum2:
                    pivot=i
                    break
        return pivot
        