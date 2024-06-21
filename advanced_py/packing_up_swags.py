class Solution(object):
    def pack_up_swags(self, n):
        #base case
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range (2, n+1):
            dp[i] = i
            j = 1
            while j * j <= i:
                # induction rule
                dp[i] = min(dp[i], dp[i - j*j] + 1) # e.g. 10个swag,3*3个放一个箱子，剩下1个放一个箱子
                j += 1

        return dp[n]

obj = Solution()
num = obj.pack_up_swags(12)
# print(num)
