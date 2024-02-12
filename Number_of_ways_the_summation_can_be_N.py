"""
Given 3 numbers {1, 3, 5}, the task is to tell the total number of ways we can
form a number N using the sum of the given three numbers.
(allowing repetitions and different arrangements)
"""

# Using Recursion
# Time complexity  - 3^N
# Space complexity - O(n) [Since stack is used in backed to store the function calls]

class Solution():
    def possible_ways(self,n):

        # base condition
        if n == 0:
            return 1

        if n < 0 :
            return 0

        return self.possible_ways(n-1) + self.possible_ways(n-3) + self.possible_ways(n-5)



    
