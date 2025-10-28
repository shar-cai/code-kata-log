'''
A prefix sum is a running total of an array, where each element is the sum of all preceding elements in the 
original array up to that index. It's a powerful technique to calculate the sum of any subarray in constant 
time (O(1) after an initial O(n) preprocessing step. For a subarray from index l to r, the sum is simply the 
prefix sum at r minus the prefix sum at (l-1). 
'''
""" 
Find Pivot Index (LC 724 Easy)
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal 
to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements 
to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""
# Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.
# Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.
# For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = [0]*(len(nums)+1)
        sumRight = [0]*(len(nums)+1)

        # prefix sum for sumLeft, iterating through nums left to right
        for i in range(len(nums)):
            sumLeft[i] = sumLeft[i-1] + nums[i]

        # prefix sum for sumRight, iterating through nums right to left
        sumRight[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            sumRight[i] = sumRight[i+1] + nums[i] 

        # find when sumLeft[i-1] = sumRight[i+1]
        for i in range(len(nums)):
            if sumLeft[i-1] == sumRight[i+1]:
                return i

        return -1        # no pivot index
    
# more efficient soln:
    def pivotIndex(self, nums: List[int]) -> int:
        # edge case: if everything after left edge of array is 0, pivot index is 0
        if(sum(nums[1::])==0):          # [start (inclusive) : stop (exclusive) : step] 
            return 0
        # check compare prefix and postfix sums in 1 for loop
        for i in range(len(nums)-1):
            if(sum(nums[:i:])==sum(nums[i+1::])):           # sum from 0 to i-1 == sum from i+1 to end
                return i
        # edge case: if everything to the left of right edge of array is 0, pivot index is len-1
        if(sum(nums[0:len(nums)-1:])==0):
            return len(nums)-1
        return -1               # no pivot index

""" 
Find the Highest Altitude (LC 1732 Easy)
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i
and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # initialize array of size n+1
        alts = [0]*(len(gain)+1)

        # prefix sum algo, iterating through gain 
        for i in range(len(gain)):
            alts[i] = alts[i-1] + gain[i]
        
        highest = max(alts)         # highest altitude
        print(alts, "high", highest)
        return highest
    
""" 
Product of Array Except Self (LC 238 Medium)
Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
# Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements
# except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
# Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*(len(nums))        # init array of same size as nums
        prefix = [0]*(len(nums)) 
        suffix = [0]*(len(nums)) 

        # prefix algo, iterating through nums from start, multiplying incrementally
        prefix[0] = nums[0]                     # index 0 is just the first num
        for i in range(1,len(nums),1):          # from index 1 to end multiply prev nums with current num
            prefix[i] = prefix[i-1] * nums[i]

        # suffix sums, iterating through nums from end, multiplying decrementally
        suffix[len(nums)-1] = nums[len(nums)-1]     # last index is just the last num
        for i in range(len(nums)-2,-1,-1):          # from last index to 0, multiply prev w current
            suffix[i] = suffix[i+1] * nums[i]

        # find producs of elements EXCEPT for element i
        answer[0] = suffix[1]                       # index 0 is suffix 1 bc excluding i aka 0
        answer[len(nums)-1] = prefix[len(nums)-2]   # last index is prefix 2nd last index
        for i in range(1,len(nums)-1,1):
            answer[i] = prefix[i-1] * suffix[i+1]   # multiply prefix and suffix

        #print(prefix, suffix, answer)
        return answer
    
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
# need to use 1 array but have 2 passes, 1 for prefix and 1 for suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res