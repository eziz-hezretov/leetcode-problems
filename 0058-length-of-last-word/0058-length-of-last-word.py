class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        temp = s.strip()
        list(s)
        for letter in reversed(temp):
            if letter == " ":
                break
            else:
                result += 1
        return result