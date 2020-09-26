'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


Following solution is Dynamic programming approach.
For more optimized search for Manacher's algorithm
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        dp = [[False for _ in range(len(s))] for i in range(len(s))]
        sindex=0
        maxlen=0
        
        for i in range(len(s)):
            dp[i][i]=True
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                sindex=i
                maxlen=1
        for l in range(2,len(s)):
            i=0
            while(i+l<len(s)):
                if s[i]==s[i+l] and dp[i+1][i+l-1]==True:
                    dp[i][i+l]=True
                    maxlen=l
                    sindex = i
                i+=1
        return s[sindex:sindex+maxlen+1]



