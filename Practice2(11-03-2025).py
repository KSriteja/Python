# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b= Counter(nums)
        a=b[0]
        k,j=1,1
        for i in nums:
                if(i==0):
                    k=k*i
                else:
                    j=j*i
        for i in range(0,len(nums)):
            if(nums[i]==0 and a==1):
                nums[i]=j
            elif((nums[i]!=0 and a==1) or a>1):
                nums[i]=0
            elif(nums[i]!=0 and a==0):
                nums[i] = j/nums[i]
        return nums