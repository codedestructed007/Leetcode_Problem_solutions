"""
given a string 'aaaabababbaaa'
Your task is to find the maximum distance between any two 'a'(s) and minimum distance between
any two 'b'(s)
distance should be measured by : |j-i| where i and j are the indeces of the
char(s) 'a' and 'b'.
return result where
result = maximum distance between two 'a'(s) + minimum ditance betweeen any two
'b'(s)
ex - 'aababbababa'
output - max(a) = 10, min(b) = 1, return 11

"""
class Solution:
    def max_min(self,s:str):
        min_b = len(s)

        # calculating maximum between two 'a's
        
        i = 0
        j = len(s)-1
        

        while i<j:
            if s[i] == 'a' and s[j] == 'a':
                max_a = j-i
                break

            elif s[i] == 'a' and s[j] != 'a':
                j-=1

            elif s[i] != 'a' and s[j] == 'a':
                i+=1

            else:
                i+=1
                j-=1

        # calculating mimimum distance between two 'b'(s)
        m = 0
        n = 1

        while n<len(s):
            if s[m] == 'b' and s[n] != 'b':
                n+=1

            elif s[m] == 'b' and s[n] == 'b':
                if (n-m) < min_b:
                    min_b = abs(n-m)

                m = n
                n+=1

            else:
                m+=1
                n+=1

        result = max_a + min_b
        
        return result
        
                
        
                
