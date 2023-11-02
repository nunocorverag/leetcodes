#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums
        
# @lc code=end

