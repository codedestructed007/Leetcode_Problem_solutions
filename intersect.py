"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
example 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

example 2
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            larger = nums1
            smaller = nums2
        else:
            larger = nums2
            smaller = nums1

        result =[]
        smaller_dic = Counter(smaller)
        larger_dic = Counter(larger)

        for num, count in smaller_dic.items():
            value = min(count, larger_dic.get(num,0)) 
            result.extend([num] * value)
        
        return result

                
                
