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