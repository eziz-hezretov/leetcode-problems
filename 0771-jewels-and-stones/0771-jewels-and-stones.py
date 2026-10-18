class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        list_jewels = list(jewels)
        list_stones = list(stones)

        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    counter += 1
        
        return counter
