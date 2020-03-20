'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Compute in O(n) time complexity and O(1) space complexity.

Given solution is by juggling approach.

'''
def computeGCD(x, y): 
        while(y): 
            x, y = y, x % y 
  
        return x 
  

class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0:
            return nums
        
        
        n=len(nums)
        g=computeGCD(k,n)
        
        
        for i in range(0,g):
            t=j=n-i-1
            temp=nums[t]
            
            while True:
                nums[j]=nums[(j-k)%n]
                if (j-k)%n == t:
                    break
                j=(j-k)%n
            nums[j]=temp
        
