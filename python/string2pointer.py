""" 
Is Subsequence (LC 392 Easy)
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
# parse through s, and parse through t to try and match chars with s
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0
        pointerT = 0

        # parse through s, comparing each char to char in t
        # when match is found, increment to move to the next char until whole substring is found or finished parsing t
        while pointerS < len(s) and pointerT < len(t):
            print(pointerS, pointerT)
            if t[pointerT] == s[pointerS]:
                pointerS += 1       # move onto next char in substring
                pointerT += 1       # move onto next char in string
            else:
                pointerT += 1       # check next char in string

        # if pointerS points to after the last index in s then the whole substring was iterated through therefore it exists in t
        if pointerS == (len(s)):
            return True
        else:
            return False
'''
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. In this scenario, 
how would you change your code?
'''
# make anoter loop to iterate thorugh all the s strings


        