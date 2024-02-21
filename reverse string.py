"""
Write a funciton that reverses a string. The input strig is given as an array
of char(s)
"""

class Solution:
    def reverseString(self,array):
        i = 0
        j= len(array)-1
        while i < j:
            array[i], array[j] = array[j],array[i]
            i+=1
            j-=1

        return array
