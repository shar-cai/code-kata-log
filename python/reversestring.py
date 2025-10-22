""" 
Reverse String (LC 344)
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
Reverse Vowels of a String (LC 345)
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