#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0
        return max_count
        
# @lc code=end

