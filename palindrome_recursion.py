"""
Write a function to check whether an array is a palindrome or not using recursion
"""

class Solution():
    def palindrome_recursion(self,nums,start,end):
        # base case
        if start >= end:
            return 'Yes, It is a Palindrome'

        # logic
        if nums[start]!= nums[end]:
            return 'Not a palindrome'
        
        # recursive call
        return self.palindrome_recursion(nums,start+1,end-1)
