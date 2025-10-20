""" 
Two Sum (LC 1)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add 
up to target.
 """
# need to check for a complement/condition w 2 items --> try storing what's missing
# one pass hashmap (good for fast lookup) --> check if target - num is already stored, then store number
# check before storing to avoid duplicates (matching # w itself)
# hash-based solutions convert search problems from O(n²) like nested loops to O(n)
class TwoSumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mydict:
                return [i, mydict[complement]]
            mydict[nums[i]] = i
        return []


""" 
Roman to Integer (LC 13)
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
 """
# solve by working the string from back to front and using a map
class Solution:
    def romanToInt(self, s: str) -> int:
        # Map single symbols to values
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev_value = 0
        
        # Process symbols from right to left
        for char in reversed(s):
            curr = values[char]
            # If current value is at least the previous, add it; otherwise subtract it
            if curr >= prev_value:
                total += curr
            else:
                total -= curr
            prev_value = curr
        
        return total
    
    def worseromanToInt(self, s: str) -> int:
        # refer to dictionary for key value pairs
        numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        s = s+"Q"       # pad the end of the string
        
        # start at end, range(start,stop,step)
        for i in range (len(s)-1,-1,-1):
            print("i=", i)
            if s[i] == "I":
                if s[i+1] == "V":
                    num -= numerals["I"]
                elif s[i+1] == "X":
                    num -= numerals["I"]
                else:
                    num += numerals["I"]
            elif s[i] == "V":
                num += numerals["V"]
            elif s[i] == "X":
                if s[i+1] == "L":
                    num -= numerals["X"]
                elif s[i+1] == "C":
                    num -= numerals["X"]
                else:
                    num += numerals["X"]
            elif s[i] == "L":
                num += numerals["L"]
            elif s[i] == "C":
                if s[i+1] == "D":
                    num -= numerals["C"]
                elif s[i+1] == "M":
                    num -= numerals["C"]
                else:
                    num += numerals["C"]
            elif s[i] == "D":
                num += numerals["D"]
            elif s[i] == "M":
                num += numerals["M"]
            else:
                num +=0
            print(num)

        return num                                              