class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        co=Counter(nums)
        res=sorted(co, key=co.get, reverse=True)
        return res[:k]
        