"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and
you may return the result in any order.
"""
class Solution:
    def intersection(self, nums1:list, nums2:list):
        return list(set(nums1).intersection(set(nums2)))
    
