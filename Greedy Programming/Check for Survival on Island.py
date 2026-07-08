from math import ceil


class Solution:
    def minimumDays(self, daysToSurvive, perDayBuyLimit, foodPerDayNeeded):
    
        totalFoodNeeded = daysToSurvive  * foodPerDayNeeded

        """
        If we need to suvive more than 6 days we need to check 
          - 6 * perDayBuyLimit <-- this is the food i can buy in a week as the job is closed on sunday
          - 7 * foodPerDayNeeded <-- this is the good i needed in a week to survice

          if canBuy < food needed to suvive then we return -1
          
        """
        if daysToSurvive > 6 and 6 * perDayBuyLimit < 7 * foodPerDayNeeded:
            return -1

        return ceil(totalFoodNeeded / perDayBuyLimit)
        
