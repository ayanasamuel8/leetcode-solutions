from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # 1. Count how many of each digit we actually have available
        available_counts = Counter(digits)
        valid_count = 0
        
        # 2. Check every possible 3-digit even number (100 to 998)
        # We step by 2 so we only look at numbers ending in 0, 2, 4, 6, 8
        for num in range(100, 1000, 2):
            # Break the number down into its 3 digits
            d1 = num // 100          # Hundreds place
            d2 = (num // 10) % 10    # Tens place
            d3 = num % 10            # Ones place
            
            # Count how many copies of each digit this specific number needs
            needed_counts = Counter([d1, d2, d3])
            
            # 3. Check if our 'digits' array has enough copies of these digits
            is_possible = True
            for digit, count in needed_counts.items():
                if available_counts[digit] < count:
                    is_possible = False
                    break
            
            # If we have enough digits to form this number, count it!
            if is_possible:
                valid_count += 1
                
        return valid_count
