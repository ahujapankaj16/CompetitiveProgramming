'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        
        wordDict = set(wordDict)
        
        dp = [False]*(len(s)+1)
        dp[0] = True
        temp=defaultdict(list)
        for i in range(len(s)):
            if dp[i]:
                for j in range(i,len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
                        temp[j].append(i)
            else:
                continue

        if dp[-1]==False:
            return result
        queue=[]
        for i in temp[len(s)]:
            queue.append([i,len(s)+1,""])
            
            
        while len(queue)!=0:
            ele = queue.pop(0)
            if ele[0]==0:
                subString=s[ele[0]:ele[1]]+" "+ele[2]
                result.append(subString.rstrip())
            else:
                subString=s[ele[0]:ele[1]]+" "+ele[2]
                for p in temp[ele[0]]:
                    queue.append([p,ele[0],subString])
        return result
