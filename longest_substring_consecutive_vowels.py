"""
Return longest substring length of consecutive vowels
ex- aaaeixuopssmnt
output= 5 (aaaei)
"""

class Solution:
    def LongestSubstringVowels(self,s:str):
        prev = 0
        forward = 0
        longest_substring_length= 0
        vowels = 'aeiou'
    
        while forward< len(s):
            if s[prev] in vowels and s[forward] not in vowels:
                if forward - prev > longest_substring_length:
                    longest_substring_length = forward-prev
                prev = forward
                forward+=1

            elif s[prev] in vowels and s[forward] in vowels:
                forward+=1

            else:
                prev +=1
                forward +=1

        # for the last case
        if (forward - prev) > longest_substring_length:
            longest_substring_length = forward - prev
    

        return longest_substring_length
