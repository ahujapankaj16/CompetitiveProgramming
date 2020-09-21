'''
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)
'''

def subsum(nums,s):
    
    dp = [[False for i in range(s+1)] for j in range(len(nums)+1)]
    
    
    for i in range(len(nums)+1):
            dp[i][0] = True
    for i in range(1,len(nums)+1):
        for j in range(1,s+1):
            
            if nums[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]          
    for i in range(s,-1,-1):
        if dp[-1][i]:
            return (i)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s=sum(stones)
        ans= s-2*subsum(stones,s//2)
        return ans
        
        

                
