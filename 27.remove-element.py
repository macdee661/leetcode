#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.



# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k+1
        
        return k
    

    
#all we truly care about is nums[:k] so that's all you really need to worry about.
#iterate through the list. when ever there is a value not equal to val, assign it to nums[k]
#increment k to keep track of the first k items

        
# @lc code=end

