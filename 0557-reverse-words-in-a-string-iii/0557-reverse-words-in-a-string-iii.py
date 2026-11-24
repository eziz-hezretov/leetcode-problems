class Solution:
    def reverseWords(self, s: str) -> str:
        
        new_list = s.split()
        newer_list = []

        print(new_list)

        for word in new_list:
            new_word = word[::-1]
            newer_list.append(new_word)

        result = " ".join(newer_list)

        return result