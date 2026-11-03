class Solution:
    def minMoves(self, nums: List[int]) -> int:

        counter = 0
        
        
        for i in nums:
            while i != max(nums):
                i += 1
                counter += 1

        return counter
