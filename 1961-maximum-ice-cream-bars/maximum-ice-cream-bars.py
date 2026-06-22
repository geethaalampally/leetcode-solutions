class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()

        count = 0
        for i in range(len(costs)):
                coins = coins - costs[i]

                if coins != 0 and coins > 0:
                    count += 1

                elif coins == 0:
                    count += 1
                    break

        return count