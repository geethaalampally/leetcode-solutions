class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:


        # Sort costs in ascending order
        costs.sort()

        count = 0

        for cost in costs:

            # Buy the current ice cream
            coins -= cost

            # Not enough coins after purchase
            if coins < 0:
                break

            # Ice cream successfully purchased
            count += 1

        return count