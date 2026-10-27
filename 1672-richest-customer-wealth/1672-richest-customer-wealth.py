class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        biggest_account = 0
        
        for account in accounts:
            if sum(account) >= biggest_account:
                biggest_account = sum(account)
            else:
                continue
        
        return biggest_account