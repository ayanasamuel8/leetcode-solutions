class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = [1 if customers[-1] == 'Y' else 0]
        n = len(customers)
        for i in range(n - 2, -1, -1):
            y.append(y[-1] + int(customers[i] == 'Y')) 
        y.reverse()
        penality = 0
        min_penality = inf
        min_pen_idx = -1
        for i in range(n):
            curr_pen = penality + y[i]
            if curr_pen < min_penality:
                min_penality = curr_pen
                min_pen_idx = i
            penality += int(customers[i] == 'N')
        if penality < min_penality:
            min_pen_idx = n
        return min_pen_idx
        