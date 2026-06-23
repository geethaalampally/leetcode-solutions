class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # sumi=0
        # n=len(mat)
        # for i in range(n):
        #     for j in range(n):
        #         if i==j or j==(n-i-1):
        #             sumi+=mat[i][j]
        # return sumi

        n=len(mat)
        sumi=0
        for i in range(n):
            sumi+=mat[i][i]
            sumi+=mat[i][n-i-1]
        if n%2==1:
            sumi-=mat[n//2][n//2]
        return sumi
                