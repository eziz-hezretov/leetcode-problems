class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        list_ransom = list(ransomNote)
        list_magazine = list(magazine)

        for char in ransomNote:
            if char in list_magazine:
                list_magazine.remove(char)
            else:
                return False
        
        return True
        
            