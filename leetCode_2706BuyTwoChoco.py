class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = float("inf") # Initizlize two variables to positive infinity
        min2 = float("inf")

        for p in prices:
            #Inside the loop, check if the current price (p) is less than the current minimum (min1). 
            #If true, update min2 to be equal to the current value of min1, 
            #and update min1 to be equal to the current price.
            if p < min1:
                min2 = min1
                min1 = p
            # If the current price is not less than min1 but is less than min2, 
            # update only min2 to be equal to the current price.
            elif p < min2:
                min2 = p
        
        leftover = money - min1 -min2

        if leftover <0:
            return money
        
        return leftover