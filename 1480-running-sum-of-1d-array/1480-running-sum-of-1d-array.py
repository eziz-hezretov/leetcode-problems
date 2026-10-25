class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        new_list = []

        for index, value in enumerate(nums):

            temp_sum = 0
            temp_index = index

            while temp_index >= 0:
                temp_sum += nums[temp_index]
                temp_index -= 1
            
            new_list.append(temp_sum)
        
        return new_list