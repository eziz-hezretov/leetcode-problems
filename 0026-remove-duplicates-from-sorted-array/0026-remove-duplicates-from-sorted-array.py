class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)

        nums[:] = sorted(seen)

        return len(seen)