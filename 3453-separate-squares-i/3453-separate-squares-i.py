class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def compute_areas(mid):
            above_area = below_area = 0.0
            for x, y, l in squares:
                top_y = y + l
                
                if top_y <= mid:  
                    below_area += l * l 
                elif y >= mid:  
                    above_area += l * l  
                else:
                    above_part = (top_y - mid) * l
                    below_part = (mid - y) * l
                    above_area += above_part
                    below_area += below_part
            
            return above_area - below_area
        
        low, high = min(y for _, y, _ in squares), max(y + l for _, y, l in squares)
        
        while high - low > 1e-5:
            mid = (low + high) / 2
            if compute_areas(mid) > 0:
                low = mid
            else:
                high = mid
        
        return round(low, 5)