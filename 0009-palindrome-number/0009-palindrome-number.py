class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        temp_number = number

        if x < 0:
            return False
        elif 0 <= x < 10:
            return True

        result = False
        counter = 0
        steps = 0
        current_step = 1

        #digit counter
        while temp_number != 0:
            temp_number = temp_number // 10
            counter += 1
        
        if counter % 2 == 0:
            steps = counter / 2
        elif counter % 2 != 0:
            steps = (counter - 1) / 2
        
        left_digit = number // (10 ** (counter - 1))
        right_digit = number % 10

        while current_step <= steps:

            if left_digit != right_digit:
                result = False
                break
            else:
                result = True
        
            current_step += 1

            left_digit = (number // (10 ** (counter - current_step))) % 10
            right_digit = (number // (10 ** (current_step - 1))) % 10

        return result

