class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []

        for i in range(len(nums)):
            profit = 0
            if i == 0 :
                profit = nums[i] 
            elif i == 1:
                profit = max(dp[i - 1], nums[i])
            else:
                profit = max(dp[i - 2]+ nums[i], dp[i - 1])
            #Save profit
            dp.append(profit)
        return max(dp)
        