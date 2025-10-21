""" 
Kids With the Greatest Number of Candies (LC 1431)
There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all 
the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
 """
# array: input an array, output an array
# For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i]
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        
        return result
    
""" 
Final Value of Variable After Performing Operations (LC 2011)
There is a programming language with only four operations and one variable X:
++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.
Given an array of strings operations containing a list of operations, 
return the final value of X after performing all the operations. 
 """
# There are only two operations to keep track of
# Use a variable to store the value after each operation
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                result +=1
            else:
                result -=1
        
        return result