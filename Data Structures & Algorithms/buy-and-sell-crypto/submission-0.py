class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        global_max_profit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                curr_max_profit=prices[right]-prices[left]
                global_max_profit=max(curr_max_profit, global_max_profit)
            else:
                left=right
            right+=1
        return global_max_profit
