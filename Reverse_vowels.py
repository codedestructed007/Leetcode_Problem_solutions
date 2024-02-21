"""
Given the string(s), revrese only all the vowels in the string and return it
"""

# Apporach-
# Two pointer -
# start with two pointer one in left most side and one at right most side
# 

class Solution:
    def reverse_vowels(self,s:str):
            # 'hello'
            # ans - 'holle'
            i = 0
            j = len(s)-1
            s= list(s)
            vowels= list('aeiouAEIOU')
            while i < j:
                if s[i] in vowels:
                    if s[j] in vowels:
                        s[i],s[j] = s[j],s[i]
                        i+=1
                        j-=1
                    else:
                        j-=1
                elif s[j] in vowels:
                    if s[i] in vowels:
                        s[j],s[i] = s[i],s[j]
                        i+=1
                        j-=1
                    else:
                        i+=1
                else:
                    i+=1
                    j-=1
            return ''.join(s)                

                
