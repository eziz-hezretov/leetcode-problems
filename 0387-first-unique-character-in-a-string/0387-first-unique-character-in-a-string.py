class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        seen = {}

        list_s = list(s)

        for char in list_s:
            if char not in seen:
                seen[char] = 0

        for char in list_s:
            for key in seen.keys():
                if char == key:
                    seen[char] += 1

        for char, count in seen.items():
            if count == 1:
                return list_s.index(char)
                break
        
        return -1

