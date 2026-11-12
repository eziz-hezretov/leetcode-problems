class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp = ""

        for word in s.split():
            temp += (word[::-1] + " ")

        return temp[:-1]