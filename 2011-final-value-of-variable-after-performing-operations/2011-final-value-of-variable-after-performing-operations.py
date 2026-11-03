class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        
        number = 0

        for item in operations:
            if item == '++X' or item == 'X++':
                number += 1
            else:
                number -= 1
        
        return number
