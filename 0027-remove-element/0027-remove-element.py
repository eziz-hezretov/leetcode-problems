class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # remove all occurences of val 
        # return nums with elements that aren't val at the front
        # return total number of elements in nums which AREN'T equal to val

        val_occurrences = 0

        for num in nums:
            if num == val:
                val_occurrences += 1


        placeholder = val_occurrences

        while placeholder > 0:
            nums.append('a')
            placeholder -= 1


        placeholder_index = 0

        while placeholder_index < len(nums):
            if nums[placeholder_index] == val:
                nums.pop(placeholder_index)
            else:
                placeholder_index += 1

        print(nums)

        num_not = len(nums) - val_occurrences
        return num_not