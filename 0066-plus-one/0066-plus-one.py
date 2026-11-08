class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            number = int("".join(map(str, digits)))
            number += 1
            digits = [int(digit) for digit in str(number)]
            
        return digits