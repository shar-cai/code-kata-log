""" 
Can Place Flowers (LC 605 Easy)
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
    
""" 
Increasing Triplet Subsequence (LC 334 Medium)
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""
# array: pase through array
# greedy: try to find triplets as soon as possible (keeping track of the smallest potential "first" and "second" numbers of the triplet as you iterate through the array)
# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # two thresholds
        tripOne = 999999999999999999999
        tripTwo = 999999999999999999999
        
        for i in range(len(nums)):
            # if i < tripOne, that is new tripOne
            if nums[i] < tripOne:
                tripOne = nums[i]
            else:
                # if i > tripOne and < tripTwo, that is new tripTwo
                if nums[i] < tripTwo and nums[i] > tripOne:
                    tripTwo = nums[i]
                else:
                    # if tripOne < tripTwo < i, triplet found
                    if tripOne < tripTwo < nums[i]: 
                        return True
            print(tripOne, tripTwo)
        return False            # no triplet found
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float("inf"), float("inf")
        for k in nums:
            if k <= i:              # need <= so we dont set j to be same num as i
                i = k
            elif k <= j:
                j = k
            else:
                return True         # bc if k is greater than i and j, then triplet found
        return False