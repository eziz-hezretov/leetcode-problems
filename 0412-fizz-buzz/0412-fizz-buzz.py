class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        fb_list = list(range(1, n + 1))
        
        for index, i in enumerate(fb_list):
            if (((i % 5) == 0) and ((i % 3) == 0)):
                fb_list[index] = "FizzBuzz"
            elif ((i % 5) == 0):
                fb_list[index] = "Buzz"
            elif ((i % 3) == 0):
                fb_list[index] = "Fizz"
            else:
                fb_list[index] = str(i)

        return fb_list