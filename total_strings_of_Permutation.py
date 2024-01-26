"""
Problem - Given a string (let say 'ABC') print all the possible permuation of the
given string
i.e.
'ABC'
'ACB'
'BCA'
'BAC'
'CAB'
'CBA'
"""
class Solution():
    def permutation(self,string:list,left:int, right:int):

        if left == right:
            print(string)
            return []


        for i in range(left , right):
            string[left], string[i] = string[i], string[left]
            self.permutation(string, left+1,right)
            string[left], string[i] = string[i], string[left]
            



"""
Note- Left should always be 0 and right should be length of the list

"""
        
