
"""
Given 3 numbers {1, 3, 5}, the task is to tell the total number of ways we can
form a number N using the sum of the given three numbers.
(allowing repetitions and different arrangements)
"""

# Using Dynamic Programming
# Time complexity - O(N)
# Space Complexity - O(N)

storage = {}
class Solution():
    def __init__(self, storage):
        self.storage= {}
        
    def all_sum(self, n):

        # base condition
        if n == 0:
            return 1

        if n < 0 :
            return 0

        if n in storage.keys():
            if storage[n] != -1:
                return storage[n]


        storage[n] = self.all_sum(n-1) + self.all_sum(n-3) + self.all_sum(n-5)
        return storage[n]


        
