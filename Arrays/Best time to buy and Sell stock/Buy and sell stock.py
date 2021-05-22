class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cur_min, max_pt = prices[0],0
        for i in range(1,len(prices)):
            if prices[i]<cur_min:
                cur_min=prices[i]
                continue
            if prices[i]-cur_min > max_pt:
                max_pt=prices[i]-cur_min
        return max(max_pt,0)