class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #create hash map with keys as numbers and values as index position

        seen = {}

        for index, num in enumerate(nums):
            looking_for = target - num

            if looking_for in seen:
                return [seen[looking_for], index]

            seen[num] = index