""" 
Move Zeroes (LC 283)
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Follow up: Could you minimize the total number of operations done?
"""
# In-place = do not allocate any space for extra array, but are allowed to modify the existing array
# 2-pointer approach: have 1 pointer for iterating the array and another that just works on the non-zero elements of the array
# solution1: brute force, track position of first 0 then swap with first nonzero after first 0
# solution2: move all nonzeros to the beginning, then fill with zeros
class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Lpointer = 0
        for Rpointer in range(len(nums)):
            # if left is 0 and right is not 0 then u swap
            if nums[Rpointer] !=0 and nums[Lpointer] == 0:
                temp = nums[Lpointer]
                nums[Lpointer] = nums[Rpointer]
                nums[Rpointer] = temp

            # if left is not 0 then move it up
            if nums[Lpointer] != 0:
                Lpointer += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        # move all nonzeros to the beginning then fill the end with 0s
        nextnonzero = 0
        
        for i in range(len(nums)):
            # if current num is nonzero, move it to nextnonzero position
            if nums[i] != 0:
                nums[nextnonzero], nums[i] = nums[i], nums[nextnonzero]         # swapping
                nextnonzero +=1
        
        # the rest (the end) 0s        
        for i in range(nextnonzero, len(nums)):
            nums[i] = 0