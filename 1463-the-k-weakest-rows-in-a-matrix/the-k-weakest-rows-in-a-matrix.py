class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []

        for i in range(len(mat)):
            arr.append((sum(mat[i]), i))

        arr.sort()

        ans = []
        for soldiers, idx in arr[:k]:
            ans.append(idx)

        return ans