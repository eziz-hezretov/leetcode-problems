class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        sorted_nums = sorted(nums)

        length = len(sorted_nums)
        
        perfect_range = list(range(length + 1))



        for num in perfect_range:
            if num not in sorted_nums:
                return num

        
