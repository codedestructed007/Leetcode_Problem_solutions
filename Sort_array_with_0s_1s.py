"""
Sort an array containing two types of elements We are given an array of 0s and
1s in random order. Segregate 0s left side and 1s right side of the array.
Traverse array only once,
Explanation -
Input : arr= [0,1,0,1,0,1,1,1,0]
output: arr =[0,0,0,0,1,1,1,1,1]
"""

class Solution():
    def sort_0s_1s(self, array):
        i = 0
        j = 1

        while j < len(array):
            if array[i] == array[j]:
                i+=1
                array[i],array[j] = array[j],array[i]
            else:                
                j +=1
                
        return array
    
