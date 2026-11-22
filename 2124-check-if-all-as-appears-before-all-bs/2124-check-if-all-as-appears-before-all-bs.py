class Solution:
    def checkString(self, s: str) -> bool:
        
        seen_b = False

        for char in s:
            if char == "b":
                seen_b = True
            elif char == "a" and seen_b == True:
                return False
                break
        
        return True