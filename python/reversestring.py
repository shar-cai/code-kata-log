""" 
Reverse String (LC 344 Easy)
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
# 2 pointers: opposite directional two-pointer approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointerA = 0
        pointerB = len(s)-1

        while pointerA < pointerB:
            #print(pointerA,pointerB)
            #swap A and B
            s[pointerA], s[pointerB] = s[pointerB], s[pointerA] 
            #move pointers in
            pointerA+=1
            pointerB-=1
        
        
""" 
Reverse Vowels of a String (LC 345 Easy)
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Ex. "IceCreAm" --> "AceCreIm"
"""
# 2 pointers: parse through the letters in the string, swap vowels when come across
# possible options:  built in string methods new_string = my_string.replace('h', 'H')
# or converting string to a list, modifying, then joining back
class Solution:
    def reverseVowels(self, s: str) -> str:
        resultList = list(s)            # converting string to a list
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        pointer1 = 0
        pointer2 = len(s)-1

        # using pointer at beginning and end until they meet in the middle
        while pointer1 < pointer2:
            #print("resultList", resultList)
            #print(pointer1,pointer2)
            # if pointer1 not a vowel move onto next letter (incrementing)
            if resultList[pointer1] not in vowels:
                pointer1 +=1
            # if a vowel, check if pointer2 is a vowel
            else:
                # if pointer2 not a vowel move onto next letter (decrementing)
                if resultList[pointer2] not in vowels:
                    pointer2 -=1
                # if a vowel (both pointers are at a vowel), then SWAP
                else:
                    temp = resultList[pointer1]
                    resultList[pointer1] = resultList[pointer2]
                    resultList[pointer2] = temp
                    # move pointers
                    pointer1 +=1
                    pointer2 -=1
            
        result = "".join(resultList)        # joining list back into string
        #print(result)

        return result

""" 
Reverse Words in a String (LC 151 Med)
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
# 2 pointers: parse through the words in the string backwards, add words to new string concat w space
# could use string method .split() to split the string by whitespace and create list of words
# strip() method removes any leading, and trailing whitespaces
class Solution:
    def reverseWords(self, s: str) -> str:
        resultList = []
        explore = len(s)-1 
        anchor = len(s)-1          # end

        # starting from end of string
        while anchor >= 0:
            # skip trailing / consecutive spaces
            while anchor >= 0 and s[anchor] == ' ':
                anchor -= 1         # move left past spaces
            if anchor < 0:          # stop after finding beginning after skipping spaces
                break

            # find the start of the current word
            explore = anchor        # start exploring from end of word
            while explore >= 0 and s[explore] != ' ':
                explore -= 1        # move left until space or start of string

            # slice the word [explore+1 : anchor+1]
            resultList.append(s[explore + 1 : anchor + 1])

            # move to the char before the space preceding this word
            anchor = explore - 1        # skip the space that precedes the word
            
        result = " ".join(resultList)        # joining list back into string
        return result
    
# using python string methods
    def reverseWords2(self, s: str) -> str:
        # divide string into a list of substrings based on a separator
        resultList = s.split()
        # reverse list
        resultList.reverse()
        # join list into string using space as separator
        result = " ".join(resultList)
        # or join the list backwards result = " ".join(resultList[::-1])
        return result