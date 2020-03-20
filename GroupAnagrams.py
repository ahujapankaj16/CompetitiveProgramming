'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Runtime: 100 ms, faster than 72.97% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.4 MB, less than 100.00% of Python3 online submissions for Group Anagrams.

*******************************************************************************
Favourite Question
*******************************************************************************
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for e in strs:
            temp = ''.join(sorted(e))
            
            if temp in result:
                result[temp].append(e)
            else:
                result[temp]=[e]
        output=[]
        for key in result:
            output.append(result[key])
            
        return output
        
        
