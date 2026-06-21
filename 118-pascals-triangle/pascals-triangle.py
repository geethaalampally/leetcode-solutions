

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def generateRow(row):
            res = [1]
            val = 1

            for c in range(1, row):
                val = val * (row - c)
                val = val // c
                res.append(val)

            return res

        ans = []

        for i in range(1, numRows + 1):
            ans.append(generateRow(i))

        return ans