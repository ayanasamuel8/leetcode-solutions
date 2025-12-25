class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        dec = 0
        n = len(happiness)
        for i in range(n):
            if happiness[i] > dec:
                total += happiness[i] - dec
                if dec < k - 1:
                    dec += 1
                else:
                    break
        return total