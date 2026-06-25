class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []

        for interval in intervals:

            # No overlap
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)

            # Overlap
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans