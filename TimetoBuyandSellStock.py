class Solution(object):
    def maxProfit(self, prices):
        # EASY QUESTION
        """
        :type prices: List[int]
        :rtype: int
        """
        # find local min and search for local max, sliding window;
        l, r = 0, 1 # Left and Right Pointers, Left = Buy, Right = Sell
        max_p = 0   # Max Profit
        
        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # if profit is bigger than current max profit assign it as new max_p
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
            
        return max_p