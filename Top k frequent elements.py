"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


class Solution:
    def TopKFrequent(self,nums:list,k:int):

        # if only one element is present in nums
        if len(nums) == 1:
            return nums

        result = []
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num]= 1

        # sort dictionary with its values
        sorted_list=sorted(frequency.items(), key = lambda x : x[1], reverse=True)

        # append top k result in result dictionary
        for i in range(k):
            result.append(sorted_list[i][0])
        return result
