class Solution:
    def climbStairs(self, n: int) -> int:
                 
        one = 0
        two = 1

        for num in range(n):
            print(num)
            temp = two
            two = one + two
            one = temp
        
        return two