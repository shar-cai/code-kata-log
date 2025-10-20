""" 
Greatest Common Divisor of Strings (LC 1071)
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
 """
# the greatest common divisor must be a prefix of each string, so we can try all prefixes
# both strings have to be made up of the same prefix in order to have a gcd (ex. ABAB and ABABAB not LELE and COCO)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_x = ""            # empty string for greatest common divisor
        
        # if the strings are not repeats of the same prefix they do not have a gcd
        if (str1 + str2) != (str2 + str1):
            return ""

        # one solution would be to iterate through sections of str1 (x = str[0:2]) and find when 
        # x*(len(str2)/len(x))=str2 aka when the prefix of str1 can build str2
        # check len(str1) % len(x) == 0 and len(str2) % len(x) == 0 bc x must build both!
        
        # OR can use gcd(len(str1), len(str2)) to find the gcd between the lengths which is the len of the prefix  
        length1 = len(str1)
        length2 = len(str2)
        # Repeatedly replace (a, b) with (b, a % b) until b becomes 0.
        while length2 != 0:
            remainder = length1 % length2
            length1 = length2
            length2 = remainder
        gcd_length = length1  # when b == 0, 'a' holds the gcd
        
        gcd_x = str1[:gcd_length]
        
        return gcd_x