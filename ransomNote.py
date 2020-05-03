'''
Problem

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true



'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        randict=dict()
        magdict=dict()
        for i in ransomNote:
            if i in randict:
                randict[i]+=1
            else:
                randict[i]=1
        for j in magazine:
            if j in magdict:
                magdict[j]+=1
            else:
                magdict[j]=1
                

        for i in randict.keys():
            if i in magdict:
                if magdict[i]<randict[i]:
                    return False
            else:
                return False
        return True
        
        
        
        
