""" 
Merge Strings Alternately (LC 1768)
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.
Return the merged string.
 """
# 2 pointers: need to parse through the letters in 2 words, so use 2 pointers (1 for each string)
# take characters from pointer A, move pointer down, take from pointer B, move pointer down, etc.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointerA = 0
        pointerB = 0
        mergedWord = ""         # empty string for merged word
        
        while pointerA < len(word1) and pointerB < len(word2):
            # add letters into mergedWord string
            mergedWord = mergedWord + word1[pointerA] + word2[pointerB]
            #print(mergedWord)
            
            # increment pointers (move them down)
            pointerA += 1
            pointerB += 1
        
        # add extra letters from longer word
        mergedWord = mergedWord + word1[pointerA:len(word1)] + word2[pointerB:len(word2)]

        #print(mergedWord)        
        return mergedWord
    