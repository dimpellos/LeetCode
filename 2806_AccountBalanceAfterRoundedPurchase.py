class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return ((104-purchaseAmount)//10) * 10 
        # if purchaseAmount % 10 == 5:
        #     purchaseAmount += 1    
        # return 100 - int(round(purchaseAmount/10, 0)) * 10