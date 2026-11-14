class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return common

            common += letter

        return common