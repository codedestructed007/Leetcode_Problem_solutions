"""
Search for an element in a given array with binary search + recursion
"""

class Solution():
    def binary_search_recursion(self, nums,value,l,r):
        m = (l + r) //2

        # base call
        if nums[m] == value:
            return m

        # logic call
        if nums[m] > value:
            r= m-1

        elif nums[m] < value:
            l = m +1
        

        return self.binary_search_recursion(nums,value,l,r)
    
