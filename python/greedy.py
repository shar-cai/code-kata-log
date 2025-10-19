""" 
Can Place Flowers (LC 605)
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule and false otherwise.
 """
# array: flowerbed is given as integer array, must not have integers adjacently
# for flower to be planted at position i: i must be empty, i-1 must be empty (or not exist),
# i+1 must be empty (or not exist)
# greedy: try to plant flowers as soon as we can
# pad beginning and end of array with 0
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add 0 at beginning and end of array so our logic checking is easier (i, i-1, i+1 all 0)
        flowerbed = [0] + flowerbed + [0]
        flowers = 0     # counter for flowers

        # traverse array from index 1 to len-2 (dont count the added 0s)
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                # plant a flower to track
                flowerbed[i] = 1
                flowers +=1
            #print(flowers, n)
        if flowers >= n:
            return True
        else:
            return False
class FasterSolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add 0 at beginning and end of array so our logic checking is easier (i, i-1, i+1 all 0)
        flowerbed = [0] + flowerbed + [0]

        # traverse array from index 1 to len-2 (dont count the added 0s)
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                # plant a flower to track
                flowerbed[i] = 1
                n -=1
        
        # return True if planted all required flowers or there were more spots (n <= 0)
        return n <= 0