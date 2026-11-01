class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        seen = {}
        number_elements = len(nums)

        for num in nums:
            if num not in seen:
                seen[num] = 0
            if num in seen:
                seen[num] += 1


        for num in seen:
            if seen[num] >= (number_elements / 2):
                return num