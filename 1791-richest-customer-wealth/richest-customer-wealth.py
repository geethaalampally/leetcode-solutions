class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        max_val=0
        for i in range(m):
            val=0
            for j in range(n):
                val+=accounts[i][j]
            max_val=max(val,max_val)
        return max_val
        