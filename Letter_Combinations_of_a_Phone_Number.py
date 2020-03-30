'''
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


'''
def generatePermutation(a,b):
        op=[]
        for i in a:
            for j in b:
                op.append(i+j)
        return op
class Solution:
    
        
    def letterCombinations(self, digits: str) -> List[str]:
        output=[]
        mapping={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if len(digits)!=0:
            output=mapping[digits[0]]
        for i in range(1,len(digits)):
                output=generatePermutation(output,mapping[digits[i]])
        return output
