class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        
        new = []

        for i in nums:
            new.append(i)

        for i in new:
            nums.append(i)
        
        return nums