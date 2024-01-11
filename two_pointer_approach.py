"""
Given an array , return True if the sum of two element is found to equal to 'X'
otherwise return False,
ex. [3,4,6,8,9,10], X= 17
return True
explanation - arr[3] + arr[4] = 17,
Hence True

note- It is not neccessary that the given array is sorted already
"""

class Solution():
    def two_pointer_technique(self,nums,X):
        nums.sort()
        i = 0
        j = len(nums) -1

        while i<j:

            if nums[i]+nums[j] < X:
                i+=1
            elif nums[i] + nums[j] == X:
                return True
            else:
                j-=1
        return False

"""
Solution explaination -
This is called Two-Pointer logic,
The basic requirement is that the array should be sorted, if not then do it first
We start with initialization two variables i and j (let say) with values assigned
as 0 and len(nums)-1 respectively (first element and last element)

if the sum of first and last element is less than the required sum(which is X)
then we increment i' value since the value at index j is already the maximum value
in the array
if reverse happens ( sum of ith index value + sum of jth index value is more than
the required sum (X) then we move the j poninter towards i direction

last case if the sum is equal to the required value then reutrn True

Advantage -
time complexity - O(n) (depends on sort function)
space complexity- O(1)
"""
