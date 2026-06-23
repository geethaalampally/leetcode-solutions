class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumi=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j or j==(n-i-1):
                    sumi+=mat[i][j]
        return sumi
        